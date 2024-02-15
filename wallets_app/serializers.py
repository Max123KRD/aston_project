from rest_framework import serializers
from wallets_app.models import Wallet
from wallets_app.utils import generate_name


class WalletListSerializer(serializers.ModelSerializer):
    """
    Serializer for list wallets
    """
    user = serializers.CharField(source="user.username")
    type = serializers.CharField(source="get_type_display")
    currency = serializers.CharField(source="get_currency_display")

    class Meta:
        model = Wallet
        fields = ["id", "user", "type", "name", "currency", "balance", "created_on", "modified_on"]


class WalletCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for create wallet
    """
    name = serializers.CharField(max_length=8, default=generate_name)
    balance = serializers.DecimalField(max_digits=100, decimal_places=2, default=0)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Wallet
        fields = (
            "id", "name", "user", "type", "currency", "balance"
        )

    def create(self, validated_data):
        if validated_data["currency"] == Wallet.CURRENCY_METHOD_RUB:
            validated_data["balance"] = 100
        else:
            validated_data["balance"] = 3
        user = self.context['request'].user
        wallet = Wallet.objects.create(**validated_data, user=user)
        wallet.save()
        return validated_data