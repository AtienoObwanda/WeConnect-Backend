from unicodedata import name
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]