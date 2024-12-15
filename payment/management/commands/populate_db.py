import random

from django.core.management import BaseCommand

from payment.models import Account, Transaction, TransactionKind


class Command(BaseCommand):

    def handle(self, *args, **options):
        phone_numbers = [
            '09123456789',
            '09123456788',
            '09123456787',
            '09123456786',
            '09123456785',
            '09123456784',
            '09123456783',
            '09123456782',
            '09123456781',
            '09123456780',
        ]

        for phone_number in phone_numbers:
            account, created = Account.objects.get_or_create(phone_number=phone_number)
            if not created:
                continue

            for _ in range(random.randint(5, 10)):
                Transaction.objects.create(
                    account=account,
                    amount=10_000 * random.randint(1, 100),
                    kind=random.choice([TransactionKind.INCOME, TransactionKind.EXPENSE]),
                )
