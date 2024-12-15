from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from payment.models import Account, Transaction


class TransactionListTest(TestCase):
    def setUp(self):
        self.account = baker.make(Account, phone_number='09121122333')
        self.transactions = baker.make(Transaction, account=self.account, _quantity=10)

    def test_get_transaction_list_successful(self):
        response = self.client.get(reverse('transactions-list'), data={'phone_number': self.account.phone_number})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['transactions']), 10)
