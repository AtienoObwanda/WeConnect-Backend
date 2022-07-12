from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('user/', views.clientDashboard, name='clientDashboard'),
    path('hotel/admin/', views.ownerDashboard, name='ownerDashboard'),
    path('bookings/room/<int:pk>/', views.addNewBooking,name='book'),
    path('new/hotel/', views.addHotel, name='new-hotel'),

]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

