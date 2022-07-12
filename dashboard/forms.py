from django import forms
from app.models import Bookings, Room, Hotel


class BookingForm(forms.ModelForm):
     class Meta:
        model = Bookings
        exclude = ['hotel', 'user', 'amount']

class HotelForm(forms.ModelForm):
     class Meta:
         model = Hotel
         exclude = ['admin']

class RoomForm(forms.ModelForm):
     class Meta:
         model = Room
         exclude = ['hotel']


