import random

from django.core.management import BaseCommand

from payment.models import Account, Transaction, TransactionKind


class Command(BaseCommand):

    def handle(self, *args, **options):
        Account.objects.all().delete()
        Transaction.objects.all().delete()
