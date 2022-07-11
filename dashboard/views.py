from django.shortcuts import render
from django.views.generic import DeleteView, ListView, UpdateView,DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from accounts.models import Client, Owner
from .forms import BookingForm
from app.models import Bookings, Room
from accounts.models import *

def clientDashboard(request):
    currentUser = request.user.client
    activeBookings = Bookings.objects.filter(user=currentUser.pk).all()


    
    return render(request, 'client.html', {'activeBookings': activeBookings})

class addBooking(LoginRequiredMixin, CreateView):
    model = Bookings
    fields = ['']
    template_name = 'booking.html'
    def form_valid(self, form):
        form.instance.hotel = self.room.hotel
        form.instance.amount = self.room.rate
        form.instance.user=self.request.user.client

        #hotel amount user phone checkin checkout 
        return super().form_valid(form)



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
    return render(request, 'owner.html')
