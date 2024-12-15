import dataclasses
from dataclasses import asdict
from typing import List

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import Account


@dataclasses.dataclass
class TransactionData:
    amount: int
    kind: str
    created_at: str


@dataclasses.dataclass
class TransactionListData:
    transactions: List[TransactionData]


class TransactionsListView(APIView):
    def get(self, request: Request):
        account = Account.objects.get(phone_number=request.query_params.get('phone_number'))

        transactions = self._get_transactions(account)
        return Response(status=status.HTTP_200_OK, data=asdict(transactions))

    @staticmethod
    def _get_transactions(account: Account) -> TransactionListData:
        transactions = account.transaction_set.all()
        return TransactionListData(transactions=[
            TransactionData(
                amount=transaction.amount,
                kind=transaction.kind,
                created_at=transaction.created_at,
            )
            for transaction in transactions
        ])
