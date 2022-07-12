from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('user/', views.clientDashboard, name='clientDashboard'),
    path('hotel/admin/', views.ownerDashboard, name='ownerDashboard'),
    path('bookings/room/<int:pk>/', views.addNewBooking,name='book'),
    path('new/hotel/', views.newHotel.as_view(), name='new-hotel'),
    path('new/room/hotel/<int:pk>/', views.newRoom.as_view(), name='newRoom'),
    path('update/hotel/<int:pk>/', views.edit_hotel, name='updateHotel'),

]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

