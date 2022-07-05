from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime as dt
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def __str__(self) :
        return self.username
        
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
   

class owner(models.Model):
    user = models.OneToOneField(User, related_name='owner', on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer', on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.IntegerField(blank=True, null=True)
    # bookings = models.ForeignKey(Bookings, null=True, on_delete=models.CASCADE)
    def __str__(self):
            return self.user.username

    
class Facility(models.Model):
    facility_name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.facility_name 
        
    
class Hotel (models.Model):
    hotel_name = models.CharField(max_length=100)
    description = models.TextField(blank= True)
    # bookings = models.CharField(max_length=100)
    facility1 = models.CharField(max_length=30, blank=True, null=True)
    facility2 = models.CharField(max_length=30, blank=True, null=True)
    facility3 = models.CharField(max_length=30, blank=True, null=True)
    facility4 = models.CharField(max_length=30, blank=True, null=True)
    facility5= models.CharField(max_length=30, blank=True, null=True)

    room1 =  models.CharField(max_length=30, blank=True, null=True)
    room1_cover = models.ImageField(upload_to='images/', blank=True, null=True)
    room1_rate = models.PositiveIntegerField(blank=True, null=True)

    room2 = models.CharField(max_length=30, blank=True, null=True)
    room2_cover = models.ImageField(upload_to='images/', blank=True, null=True)
    room2_rate = models.PositiveIntegerField(blank=True, null=True)

    room3 =  models.CharField(max_length=30, blank=True, null=True)
    room3_cover = models.ImageField(upload_to='images/',blank=True, null=True)
    room3_rate = models.PositiveIntegerField(blank=True, null=True)

    room4 =  models.CharField(max_length=30, blank=True, null=True)
    room4_cover = models.ImageField(upload_to='images/', blank=True, null=True)
    room4_rate = models.PositiveIntegerField(blank=True, null=True)

    cover_image = models.ImageField(upload_to='images/')
    admin = models.ForeignKey(owner, on_delete=models.CASCADE)
   
        
    def __str__(self):
        return self.hotel_name
    
    def create_hotel(self):
        self.save
    
    @classmethod
    def delete_hotel(cls, hotel_name):
        cls.objects.filter(hotel_name=hotel_name).delete()
    
    @classmethod
    def find_hotel(cls, search_term):
        hotels = cls.cls.objects.filter(hotel_name__icontains = search_term)
        return hotels
    
    
    def update_hotel(self, hotel_name):
        self.hotel_name = hotel_name
        self.save()
class Rooms (models.Model):
    name = models.CharField(max_length=100)
    rate = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    hotel= models.ForeignKey(Hotel,  on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    def create_room(self):
        self.save

class Booking(models.Model):
    hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    amount = models.ForeignKey(Rooms,  on_delete=models.CASCADE)
    user =  models.ManyToManyField(Customer, related_name='bookings')
    date = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.date                  
    
