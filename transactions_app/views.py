# Create your views here.
from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import Transaction


class TransactionView(APIView):
    """
        List all transactions for current user with GET
        Create new transaction with POST
    """
    permission_classes = ()

    def get(self, request):
        transactions = Transaction.objects.filter(Q(sender__user=request.user) | Q(receiver__user=request.user))
        serializer = serializers.TransactionListSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.TransactionCreateSerializer(data=request.data,
                                                             context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetailView(APIView):
    permission_classes = ()

    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        transaction = self.get_object(pk)
        serializer = serializers.TransactionListSerializer(transaction)
        return Response(serializer.data)


class TransactionWalletView(APIView):
    permission_classes = ()

    def get(self, request, wallet_name):
        transactions = Transaction.objects.filter(Q(receiver__name=wallet_name) | Q(sender__name=wallet_name))
        serializer = serializers.TransactionListSerializer(transactions, many=True)
        return Response(serializer.data)