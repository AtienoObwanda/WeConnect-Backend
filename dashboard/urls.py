from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('user/', views.clientDashboard, name='clientDashboard'),
    path('hotel/admin/', views.ownerDashboard, name='ownerDashboard'),
    path('bookings/room/<int:pk>/', views.addNewBooking,name='book'),
<<<<<<< HEAD
    path('new/hotel/', views.new_hotel, name='new-hotel'),
=======
    path('new/hotel/', views.newHotel.as_view(), name='new-hotel'),
    path('new/room/hotel/<int:pk>/', views.newRoom.as_view(), name='newRoom'),
>>>>>>> b62cfa42d219f9e7fabcf59708d8ea293110a9d7

]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

