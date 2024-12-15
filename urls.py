from django.contrib import admin
from django.urls import path

from payment.views import TransactionsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/', TransactionsListView.as_view(), name='transactions-list'),
]
