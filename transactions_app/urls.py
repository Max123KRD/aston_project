from django.urls import path
from . import views


urlpatterns = [
    path("", views.TransactionView.as_view()),
    path("<int:pk>/", views.TransactionDetailView.as_view()),
    path("<str:wallet_name>/", views.TransactionWalletView.as_view())
]