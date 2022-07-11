from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from PIL import Image


class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField()


class Owner(models.Model):
    user = models.OneToOneField(User, related_name='owner', on_delete = models.CASCADE, primary_key = True)
    def __str__(self):
            return self.user.first_name

class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='client',primary_key = True) 

    def __str__(self):
        return self.user.first_name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField()
    address = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)

    def save_profile(self):
        self.save()
