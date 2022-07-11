from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('user/', views.clientDashboard, name='clientDashboard'),
    path('hotel/admin/', views.ownerDashboard, name='ownerDashboard'),

    
]