from django.urls import path, include

from . import views
from .views import (CustomerSignupView, HotelAdminSignupView, AddHotel, GetHotel,  HotelList,
DeleteHotel, UpdateHotel, AddRoom,AddBooking,BookingList,
 CustomAuthToken, LogoutView, AdminOnlyView, CustomerOnlyView)

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   
    path('', views.home),
    path('signup/customer/', CustomerSignupView.as_view()),
    path('signup/admin/', HotelAdminSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),

    path('customer/dashboard/<int:pk>/', CustomerOnlyView.as_view(), name='customer-dashboard'),
    # path('customer/dashboard/', CustomerOnlyView.as_view(), name='customer-dashboard'),

    path('admin/dashboard/', AdminOnlyView.as_view(), name='admin-dashboard'),

    path('hotel-detail/<int:pk>/', GetHotel.as_view(), name='hotel-detail'), # Configure api request

    path('delete-hotel/<int:pk>/', DeleteHotel.as_view(), name=' deleteHotel'),
    path('update-hotel/<int:pk>/', UpdateHotel.as_view(), name='updateHotel'),
    
    path('new-hotel/', AddHotel.as_view(), name='newHotel'), # Configure api request => to be configured inside admindashboard

    path('new-room/', AddRoom.as_view(), name='newRoom'), # Configure api request => to be configured inside admindashboard

    path('new-booking/', AddBooking.as_view(), name='newBooking'), # Configure api request-to be configured inside customer dashboard
    
    path('hotels/', HotelList.as_view(), name='hotels'), # Configure api request
    path('bookings/', BookingList.as_view(), name='bookings'), # Configure api request



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    # urlpatterns+= [path('hotels',  HotelList.as_view(), name='hotels'),] # accepts any urls otherthan above 
