from django.http import Http404
from rest_framework.exceptions import ValidationError
from django.db import transaction
from wallets_app.models import Wallet


@transaction.atomic
def send_money(sender_wallet_name, receiver_wallet_name, transfer_amount, commission):
    sender = Wallet.objects.get(name=sender_wallet_name)
    receiver = Wallet.objects.get(name=receiver_wallet_name)
    if sender.balance - transfer_amount - commission >= 0:
        sender.balance = sender.balance - transfer_amount - commission
        sender.save()
        receiver.balance = receiver.balance + transfer_amount
        receiver.save()
    else:
        raise ValidationError("Not enough money for transaction")


def get_user_from_wallet_name(wallet_name):
    try:
        return Wallet.objects.get(name=wallet_name)
    except Wallet.DoesNotExist:
        raise Http404


def get_wallet_currency_from_wallet_name(wallet_name):
    try:
        return Wallet.objects.get(name=wallet_name).currency
    except Wallet.DoesNotExist:
        raise Http404