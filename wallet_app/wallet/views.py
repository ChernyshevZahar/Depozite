from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet
from .serializers import WalletOperationSerializer, WalletBalanceSerializer

class WalletOperationView(APIView):
    def post(self, request, wallet_id):
        serializer = WalletOperationSerializer(data=request.data)
        if serializer.is_valid():
            operation_type = serializer.validated_data['operation_type']
            amount = serializer.validated_data['amount']
            with transaction.atomic():
                wallet, created = Wallet.objects.select_for_update().get_or_create(id=wallet_id)
                if operation_type == 'DEPOSIT':
                    wallet.balance += amount
                elif operation_type == 'WITHDRAW':
                    if wallet.balance < amount:
                        return Response({"error": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)
                    wallet.balance -= amount
                wallet.save()
                return Response({"balance": wallet.balance}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletBalanceView(APIView):
    def get(self, request, wallet_id):
        wallet = Wallet.objects.filter(id=wallet_id).first()
        if wallet:
            serializer = WalletBalanceSerializer(wallet)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)