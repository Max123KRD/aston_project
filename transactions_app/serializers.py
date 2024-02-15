from decimal import Decimal

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Transaction
from .utils import send_money, get_user_from_wallet_name, get_wallet_currency_from_wallet_name


class TransactionListSerializer(serializers.ModelSerializer):
    """
    Serializer for list or detail transactions
    """
    sender = serializers.CharField(source="sender.name")
    receiver = serializers.CharField(source="receiver.name")
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Transaction
        fields = ["id", "sender", "receiver", "transfer_amount", "commission", "status", "timestamp"]


class TransactionCreateSerializer(serializers.ModelSerializer):
    commission = serializers.DecimalField(max_digits=100, decimal_places=2, default=0)
    status = serializers.CharField(max_length=1, default=2)
    sender = serializers.CharField(max_length=8)
    receiver = serializers.CharField(max_length=8)

    class Meta:
        model = Transaction
        fields = ("sender", "receiver", "transfer_amount", "commission", "status")

    def create(self, validated_data):
        COMMISSION = Decimal(0.1)
        sender_wallet_name = validated_data["sender"]
        receiver_wallet_name = validated_data["receiver"]
        sender_user = get_user_from_wallet_name(sender_wallet_name)
        sender_currency = get_wallet_currency_from_wallet_name(sender_wallet_name)
        receiver_user = get_user_from_wallet_name(receiver_wallet_name)
        receiver_currency = get_wallet_currency_from_wallet_name(receiver_wallet_name)
        if sender_currency == receiver_currency:
            if sender_user != receiver_user:
                validated_data["commission"] = validated_data["transfer_amount"] * COMMISSION
            try:
                send_money(sender_wallet_name, receiver_wallet_name,
                           validated_data["transfer_amount"], validated_data["commission"])
                validated_data["status"] = Transaction.STATUS_METHOD_PAID
            except Exception as E:
                raise ValidationError(f"Transaction error {E}")

        else:
            validated_data["status"] = Transaction.STATUS_METHOD_FAILED
        transaction = Transaction.objects.create(
            transfer_amount=validated_data["transfer_amount"], commission=validated_data["commission"],
            status=validated_data["status"], sender=sender_user, receiver=receiver_user)
        transaction.save()
        return validated_data