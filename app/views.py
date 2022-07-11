from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import *

def home(request):
    return render(request, 'home.html')

def hotels(request):
    hotels = Hotel.objects.all()

    return render(request, 'hotels.html', {'hotels':hotels})


class HotelDetailList(APIView):
    permission_classes = (AllowAny,)
    renderer_classes= [TemplateHTMLRenderer]
    template_name='hotelPage.html'

    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        rooms = Room.objects.filter(hotel_id=pk)
        
        return Response({'hotel': hotel, 'rooms': rooms})