from django.shortcuts import render
from django.views.generic import DeleteView, ListView, UpdateView,DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from accounts.models import Client, Owner
from app.models import Bookings
from accounts.models import *

def clientDashboard(request):
    currentUser = request.user.client

    
    return render(request, 'client.html')

class addNewBooking(LoginRequiredMixin, CreateView):
    model = Bookings
    fields = ['']
    template_name = 'members/addZone.html'
    def form_valid(self, form):
        form.instance.user=self.request.user.client
        return super().form_valid(form)


def ownerDashboard(request):
    return render(request, 'owner.html')
