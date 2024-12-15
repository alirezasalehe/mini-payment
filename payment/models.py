from django.db import models

class Account(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.phone_number


class TransactionKind(models.TextChoices):
    INCOME = "income", "Income"
    EXPENSE = "expense", "Expense"


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    kind = models.CharField(max_length=10, choices=TransactionKind.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({'+' if self.kind == TransactionKind.INCOME else '-'}{self.amount})"
