from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from dashboard.views import addBooking


urlpatterns = [
    path('user/', views.clientDashboard, name='clientDashboard'),
    path('hotel/admin/', views.ownerDashboard, name='ownerDashboard'),
    path('add-booking/', addBooking.as_view(), name='addBooking'),
    path('bookings/room/<int:pk>/', views.addNewBooking,name='book'),
    # path('hotel', views.hotel, name='hotel'),
    # path('new/hotel$', views.new_hotel, name='new-hotel'),

]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

