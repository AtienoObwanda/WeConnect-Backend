from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('dashboard/', views.clientDashboard, name='dashboard'),
    path('dashboard/', views.ownerDashboard, name='dashboard'),

    
]