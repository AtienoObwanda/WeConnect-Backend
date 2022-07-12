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
            booking.save()
            print(room.rate)
            return redirect('hotelPage', pk)
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form, "room": room, "user": current_user})



def ownerDashboard(request):
  current_user = request.user.owner

  return render(request, 'owner.html')


      # hotel.save()
      
      
class newHotel(LoginRequiredMixin, CreateView):
    model = Hotel
    fields = ['hotel_name','description','tagline','cover_image']
    template_name = 'templates/postHotel.html'
    def form_valid(self, form):
        form.instance.admin=self.request.user.owner
        return super().form_valid(form)   
  
@login_required
def addHotel(request):
  current_user = request.user.owner
  form =  HotelForm(request.POST)
    # room = Room.objects.get(pk=pk)
  if request.method == 'POST':
    form =  HotelForm(request.POST)
    if form.is_valid():
      hotel = form.save(commit=False)
      hotel.admin.set([request.user.owner])
      hotel.save()
      return redirect('ownerDashboard')
    else:
        form = HotelForm()
        return render(request, 'posthotel.html', {'form': form, 'user' : current_user})


@login_required
def addRoom(request,pk):
  current_user = request.user.owner
  form =  HotelForm(request.POST)
  hotel = Hotel.objects.get(pk=pk)
  if request.method == 'POST':
    form =  RoomForm(request.POST)
    if form.is_valid():
      room = form.save(commit=False)
      room.hotel=hotel
      room.save()
      return redirect('ownerDashboard')
    else:
        form = HotelForm()
        return render(request, 'newRoom.html', {'form': form, 'user' : current_user, 'hotel' : hotel})