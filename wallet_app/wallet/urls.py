from django.urls import path
from wallet.views import WalletOperationView, WalletBalanceView

urlpatterns = [
    path('api/v1/wallets/<str:wallet_id>/operation', WalletOperationView.as_view(), name='wallet-operation'),
    path('api/v1/wallets/<str:wallet_id>', WalletBalanceView.as_view(), name='wallet-balance'),
]