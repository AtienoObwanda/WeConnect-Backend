from django.shortcuts import render


from django.http import Http404, request
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import CustomerSignupSerializer, HotelAdminSignupSerializer, UserSerializer, HotelSerializer, FacilitySerializer, RoomSerializer, BookingSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView

from .permissions import IsCustomerUser, IsHotelAdminUser
from .models import *

class CustomerSignupView(generics.GenericAPIView):
    serializer_class=CustomerSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })


class HotelAdminSignupView(generics.GenericAPIView):
    serializer_class=HotelAdminSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account created successfully"
        })

class CustomAuthToken(ObtainAuthToken): # Login for both admin and customer accounts
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_owner':user.is_owner
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class AdminOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsHotelAdminUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class CustomerOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsCustomerUser]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

#Create Hotel
class AddHotel(APIView):
    def get(self, request, format=None):
        hotels = Hotel.objects.all()
        # admin = request.user.owner
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = HotelSerializer(data=request.data)
        # request.data['admin'] = request.user.id 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Fetch all Hotel information
class HotelList(APIView):
    def get(self, request, format=None):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)


# Update Hotel information
class UpdateHotel(APIView):
    def get_object(self, pk):
        try:
            return Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        hotel = self.get_object(pk)
        serializer = HotelSerializer(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Hotel information
class DeleteHotel(APIView):
    def get_object(self, pk):
        try:
            return Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            raise Http404
            
    def delete(self, request, pk, format=None):
        hotel = self.get_object(pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Fetch single hotel information
class GetHotel(APIView):
    def get_object(self, pk):
        try:
            return Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hotel = self.get_object(pk)
        rooms = Rooms.objects.filter(hotel=hotel.id).all()
        serializer = HotelSerializer(hotel) #, RoomSerializer(rooms)
        # serializer = RoomSerializer(rooms)
        return Response(serializer.data)

#Create Room
class AddRoom(APIView):
    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# Fetch Room information

# Update Room information

# Delete Room information


#Create Facility 
class AddFacility(APIView):
    def post(self, request, format=None):
        serializer = FacilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Fetch Facility information

# Update Facility information

# Delete Facility information



#Create Booking
class AddBooking(APIView):
    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Fetch Booking information

# Update Booking information

# Delete Booking information






    

def home(request):
    return render(request, 'home.html')