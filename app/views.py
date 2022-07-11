from django.shortcuts import render
from rest_framework.response import Response

from app.models import *

def home(request):
    return render(request, 'home.html')

def hotels(request):
    hotels = Hotel.objects.all()

    return render(request, 'hotels.html', {'hotels':hotels})


