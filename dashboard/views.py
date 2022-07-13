import os
import sendgrid
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.shortcuts import render
from django.views.generic import DeleteView, ListView, UpdateView,DetailView, CreateView
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string


from accounts.models import Client, Owner
from .forms import BookingForm
from app.models import Bookings, Hotel, Room
from accounts.models import *


def clientDashboard(request):
    currentUser = request.user.client
    activeBookings = Bookings.objects.filter(user=currentUser.pk).all()    
    return render(request, 'client.html', {'activeBookings': activeBookings})

@login_required
def addNewBooking(request, pk):
    current_user = request.user.client
    room = Room.objects.get(pk=pk)
    # room = Room.objects.filter(pk=pk)
    if request.method == 'POST':
        form =  BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.hotel = room.hotel
            booking.amount = room
            booking.save()
            booking.user.set([request.user.client])
            Uemail = form.cleaned_data['email']
            Uname = form.cleaned_data['fullName']
            message = Mail(
                from_email='communications.weconnect@gmail.com',
                to_emails=[Uemail],
                subject='We Connect Account Created Sucessfully!',
                html_content='Hey, Your Reservation has been added...')
            message.dynamic_template_data = {
            'first_name': Uname,
                    }
            message.template_id =  'd-49b7616b7d17464893ec4808a21ce382'
            booking.save()
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)
            # return redirect('hotelPage', pk)
            return redirect('clientDashboard')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form, "room": room, "user": current_user})



def ownerDashboard(request):
  currentUser = request.user.owner
  hotels = Hotel.objects.filter(admin=currentUser.pk).all() 
  # bookings 
  bookings = Bookings.objects.filter(hotel__id__in = hotels).all()
  count = bookings.count()
  books  = list(bookings)
  print(books)
  sum = 0
  for book in books:
    print(book.amount.rate)
    sum+=book.amount.rate
  print(sum)
  
  # rooms 
  rooms = Room.objects.filter(hotel__id__in = hotels).all()

  return render(request, 'owner.html', { 'hotels':hotels, 'rooms':rooms, 'bookings':bookings, 'count':count, 'sum':sum})
      
class newHotel(LoginRequiredMixin, CreateView):
    model = Hotel
    fields = ['hotel_name','description','tagline','cover_image']
    template_name = 'posthotel.html'
    def form_valid(self, form):
        form.instance.admin=self.request.user.owner
        return super().form_valid(form)   

class newRoom(LoginRequiredMixin, CreateView):
    model = Room
    fields = ['name','tagline','rate','image','hotel']
    template_name = 'newRoom.html'
    def form_valid(self,form):
        # currentUser = self.request.user.owner
        # hotel = Hotel.objects.filter(admin=currentUser.pk).all()
        return super().form_valid(form)  

def edit_hotel(request, pk):
    current_user=request.user.owner
    if request.method=="POST":
        instance = Hotel.objects.get(pk=pk)
        form =HotelForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            hotel = form.save(commit = False)
            hotel.admin = current_user
            hotel.save()
        return redirect('ownerDashboard')
    elif Hotel.objects.get(pk=pk):
        hotel = Hotel.objects.get(pk=pk)
        form = HotelForm(instance=hotel)
    else:
        form = HotelForm()
    return render(request,'posthotel.html',{"form":form})

def delete_hotel(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    hotel.delete()
    return redirect('ownerDashboard')


def delete_room(request, pk):
    room = Room.objects.get(pk=pk)
    room.delete()
    return redirect('ownerDashboard')

def del_booking(request, pk):
    booking = Bookings.objects.get(pk=pk)
    booking.delete()
    return redirect('clientDashboard')