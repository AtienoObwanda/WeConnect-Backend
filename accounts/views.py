import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.shortcuts import render
from django.views.generic import DeleteView, ListView, UpdateView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage



from .models import *
from .forms import *


def clientDashboar(request):

    return render(request, 'register.html')


def ownerDashboard(request):
    return render(request, 'login.html')


class ClientReg(CreateView):
    model = User
    form_class = ClientRegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        Uemail = form.cleaned_data['email']
        Uname = form.cleaned_data['username']
        fName = form.cleaned_data['first_name']
        lName = form.cleaned_data['last_name']
        message = Mail(
            from_email='communications.weconnect@gmail.com',
            to_emails=[Uemail],
            subject='We Connect Account Created Sucessfully!',
            html_content='Hey, Your We Connect Account has been created successfully...'
        )
        message.dynamic_template_data = {
            'first_name': fName,
            'last_name': lName,
            'unique_name': Uname,
            'email':Uemail,
            'sender_name': 'We Connect',
            'sender_address': '00200',
            'sender_city': 'Nairobi, Kenya'
        }
        message.template_id =  'd-ddb091bebde04c108a96a9e15a65b87'

        user = form.save()
        
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        login(self.request, user)
        return redirect('login')
    


def loginClient(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('clientDashboard')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html',
                  context={'form': AuthenticationForm()})


class AdminReg(CreateView):
    model = User
    form_class = OwnerRegisterForm
    template_name = 'admin-register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admin-login')


def loginAdmin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ownerDashboard')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'admin-login.html',
                  context={'form': AuthenticationForm()})


def profile(request):
    Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.instance.user = request.user
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('clientDashboard')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
