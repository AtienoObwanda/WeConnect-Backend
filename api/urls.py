from django.urls import path, include

from . import views
from .views import (CustomerSignupView, HotelAdminSignupView, AddHotel, GetHotel,  HotelList,
DeleteHotel, UpdateHotel,
 CustomAuthToken, LogoutView, AdminOnlyView, CustomerOnlyView)

urlpatterns = [
   
    path('', views.home),
    path('signup/customer/', CustomerSignupView.as_view()),
    path('signup/admin/', HotelAdminSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('customer/dashboard/', CustomerOnlyView.as_view(), name='customer-dashboard'),
    path('admin/dashboard/', AdminOnlyView.as_view(), name='admin-dashboard'),

    path('hotels/', HotelList.as_view(), name='hotels'),
    path('hotel-detail/', GetHotel.as_view(), name='hotel-detail'),
    path('delete-hotel/', DeleteHotel.as_view(), name=' deleteHotel'),
    path('update-hotel', UpdateHotel.as_view(), name='updateHotel'),
    path('new-hotel', AddHotel.as_view(), name='newHotel'),

]