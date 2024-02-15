from django.contrib.auth.models import User
from django.test import TestCase
import unittest
from wallets_app.models import Wallet
from wallets_app.serializers import WalletListSerializer, WalletCreateSerializer
from wallets_app.utils import generate_name


name1 = generate_name()
name2 = generate_name()


class WalletSerializerTestCase(TestCase):
    def test_list_wallets(self):
        user = User.objects.create(username="testuser", email="testuser@test.test")
        wallet_1 = Wallet.objects.create(user=user, name=name1,
                                         type="1", currency="1")
        wallet_2 = Wallet.objects.create(user=user, name=name2,
                                         type="1", currency="1")
        data = WalletListSerializer([wallet_1, wallet_2], many=True).data
        expected_data = [
            {
                "id": wallet_1.id,
                "user": "testuser",
                "type": "Visa",
                "name": name1,
                "currency": "RUB",
                "balance": "0.00",
                "created_on": wallet_1.created_on.strftime("%Y-%m-%d %H:%M:%S"),
                "modified_on": wallet_1.modified_on.strftime("%Y-%m-%d %H:%M:%S"),
            },
            {
                "id": wallet_2.id,
                "user": "testuser",
                "type": "Visa",
                "name": name2,
                "currency": "RUB",
                "balance": "0.00",
                "created_on": wallet_2.created_on.strftime("%Y-%m-%d %H:%M:%S"),
                "modified_on": wallet_2.modified_on.strftime("%Y-%m-%d %H:%M:%S"),
            },
        ]
        self.assertEqual(expected_data, data)