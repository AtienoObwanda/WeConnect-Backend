from unicodedata import name
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hotels', views.hotels, name='hotels'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
