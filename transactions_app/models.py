# Create your models here.
from django.db import models

from wallets_app.models import Wallet


class Transaction(models.Model):
    STATUS_METHOD_PAID = "1"
    STATUS_METHOD_FAILED = "2"
    STATUS_TRANSACTION = (
        (STATUS_METHOD_PAID, "PAID"),
        (STATUS_METHOD_FAILED, "FAILED"),
    )
    sender = models.ForeignKey(Wallet, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Wallet, related_name="receiver", on_delete=models.CASCADE)
    transfer_amount = models.DecimalField(max_digits=100, decimal_places=2)
    commission = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    status = models.CharField(choices=STATUS_TRANSACTION, max_length=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp}"