from django.urls import path, include

from . import views
from .views import (CustomerSignupView, HotelAdminSignupView, AddHotel, GetHotel,  HotelList,
DeleteHotel, UpdateHotel, AddRoom,AddBooking,BookingList,
 CustomAuthToken, LogoutView, AdminOnlyView, CustomerOnlyView)

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   
    path('signup/customer/', CustomerSignupView.as_view()),
    path('signup/admin/', HotelAdminSignupView.as_view()),
    path('login/',CustomAuthToken.as_view()),
    path('logout/', LogoutView.as_view()),

    path('customer/dashboard/<int:pk>/', CustomerOnlyView.as_view()),

    path('admin/dashboard/', AdminOnlyView.as_view()),

    path('hotel-detail/<int:pk>/', GetHotel.as_view()), # Configure api request

    path('delete-hotel/<int:pk>/', DeleteHotel.as_view()),
    path('update-hotel/<int:pk>/', UpdateHotel.as_view()),
    
    path('new-hotel/', AddHotel.as_view()), # Configure api request => to be configured inside admindashboard

    path('new-room/', AddRoom.as_view()), # Configure api request => to be configured inside admindashboard

    path('new-booking/', AddBooking.as_view()), # Configure api request-to be configured inside customer dashboard
    
    path('hotels/', HotelList.as_view()), # Configure api request
    path('bookings/', BookingList.as_view()), # Configure api request



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    # urlpatterns+= [path('hotels',  HotelList.as_view(), name='hotels'),] # accepts any urls otherthan above 
