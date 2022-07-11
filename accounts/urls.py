from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import ClientReg

from . import views

urlpatterns = [
    path('register/', ClientReg.as_view(), name='register'),
    path('login/', views.loginClient, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

