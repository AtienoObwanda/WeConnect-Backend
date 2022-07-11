from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('dashboard/user/', views.clientDashboard, name='clientDashboard'),
    path('dashboard/hotel/admin/', views.ownerDashboard, name='ownerDashboard'),

    
]