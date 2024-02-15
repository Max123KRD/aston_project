# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Wallet
from .serializers import WalletListSerializer, WalletCreateSerializer


class WalletView(APIView):
    """
    List all wallets with GET
    Create new wallet with POST
    """
    permission_classes = ()
    MAX_WALLETS = 5

    def get(self, request):
        wallets = Wallet.objects.all()
        serializer = WalletListSerializer(wallets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WalletCreateSerializer(data=request.data,
                                            context={
                                                'request': request
                                            }
                                            )
        count_wallets = Wallet.objects.filter(user=request.user).count()
        if count_wallets >= self.MAX_WALLETS:
            return Response({"max_wallets": self.MAX_WALLETS}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WalletDetailFromNameView(APIView):
    """
    Retrieve and delete a wallets instance.
    """
    permission_classes = ()

    def get_object(self, name):
        try:
            return Wallet.objects.get(name=name)
        except Wallet.DoesNotExist:
            raise Http404

    def get(self, request, name):
        wallet = self.get_object(name)
        serializer = WalletListSerializer(wallet)
        return Response(serializer.data)

    def delete(self, request, name):
        wallet = self.get_object(name)
        wallet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)