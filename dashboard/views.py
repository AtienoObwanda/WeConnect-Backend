from django.shortcuts import render
from django.views.generic import DeleteView, ListView, UpdateView,DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from accounts.models import *

def clientDashboard(request):
    
    return render(request, 'client.html')



def ownerDashboard(request):
    return render(request, 'owner.html')
