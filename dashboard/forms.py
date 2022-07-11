from django import forms
from app.models import Bookings, Room


class BookingForm(forms.ModelForm):
     class Meta:
        model = Bookings
        exclude = ['hotel', 'user', 'amount']