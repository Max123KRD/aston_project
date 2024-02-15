from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from wallets_app.models import Wallet
from wallets_app.serializers import WalletListSerializer
from wallets_app.utils import generate_name


name1 = generate_name()
name2 = generate_name()


class WalletsApiTestCase(APITestCase):
    def test_get(self):
        user = User.objects.create(username="testuser", email="testuser@test.test")
        wallet_1 = Wallet.objects.create(name=name1, user=user,
                                         type="1", currency="1", balance=100)
        wallet_2 = Wallet.objects.create(name=name2, user=user,
                                         type="1", currency="1", balance=100)
        url = reverse("wallets")
        response = self.client.get(url)
        serializer_data = WalletListSerializer([wallet_1, wallet_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)