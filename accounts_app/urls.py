from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.UserListView.as_view(), name='account_list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='account_detail'),
    path('register/', views.UserCreateView.as_view(), name='account_create'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]