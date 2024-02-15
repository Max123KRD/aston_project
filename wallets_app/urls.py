from django.urls import path
from . import views

urlpatterns = [
    path('', views.WalletView.as_view(), name="wallets"),
    path('<str:name>/', views.WalletDetailFromNameView.as_view(), name="wallet_detail"),
]