from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Wallet

class WalletTests(APITestCase):
    def test_perform_operation(self):
        wallet_id = 'test_wallet'
        url = reverse('wallet-operation', args=[wallet_id])
        data = {'operation_type': 'DEPOSIT', 'amount': 1000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'balance': 1000})

        data = {'operation_type': 'WITHDRAW', 'amount': 500}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'balance': 500})

    def test_get_balance(self):
        wallet_id = 'test_wallet'
        Wallet.objects.create(id=wallet_id, balance=500)
        url = reverse('wallet-balance', args=[wallet_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'balance': '500.00'})

    def test_withdraw_more_than_balance(self):
        wallet_id = 'test_wallet'
        Wallet.objects.create(id=wallet_id, balance=500)
        url = reverse('wallet-operation', args=[wallet_id])

        data = {'operation_type': 'WITHDRAW', 'amount': 1000}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {'error': 'Insufficient funds'})