# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Wallet(models.Model):
    PAYMENT_METHOD_VISA = "1"
    PAYMENT_METHOD_MASTERCARD = "2"
    TYPE_CHOICES = (
        (PAYMENT_METHOD_VISA, "Visa"),
        (PAYMENT_METHOD_MASTERCARD, "Mastercard"),
    )
    CURRENCY_METHOD_RUB = "1"
    CURRENCY_METHOD_USD = "2"
    CURRENCY_METHOD_EUR = "3"
    CURRENCY_CHOICES = (
        (CURRENCY_METHOD_RUB, "RUB"),
        (CURRENCY_METHOD_USD, "USD"),
        (CURRENCY_METHOD_EUR, "EUR"),
    )
    name = models.CharField(max_length=8, unique=True)
    user = models.ForeignKey(User, related_name="wallets",on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE_CHOICES, max_length=1, default=1)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=1, default=1)
    balance = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_on} - {self.get_type_display()}"