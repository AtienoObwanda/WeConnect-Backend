from django.urls import path, include

from . import views
from .views import (CustomerSignupView, HotelAdminSignupView,
 CustomAuthToken, LogoutView, AdminOnlyView, CustomerOnlyView)

urlpatterns = [
   
    path('', views.home),
    path('signup/customer/', CustomerSignupView.as_view()),
    path('signup/admin/', HotelAdminSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('freelance/dashboard/', CustomerOnlyView.as_view(), name='customer-dashboard'),
    path('client/dashboard/', AdminOnlyView.as_view(), name='admin-dashboard'),
]