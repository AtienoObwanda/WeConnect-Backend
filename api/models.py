from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime as dt


class User(AbstractUser):
    is_hotelAdmin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
   

class HotelAdmin(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer', on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.IntegerField(blank=True, null=True)
    # bookings = models.ForeignKey(Bookings, null=True, on_delete=models.CASCADE)
    def __str__(self):
            return self.user.name



class Rooms (models.Model):
    name = models.CharField(max_length=100)
    rate = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    hotel =  models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def create_room(self):
        self.save
    
class Facility(models.Model):
    facility_name = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.facility_name 
        
    
class Hotel (models.Model):
    hotel_name = models.CharField(max_length=100)
    rooms= models.ForeignKey(Rooms,  on_delete=models.CASCADE)
    description = models.TextField(blank= True)
    facility = models.ForeignKey(Facility,  on_delete=models.CASCADE)
    bookings = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='images/')
    admin = models.ForeignKey(HotelAdmin, on_delete=models.CASCADE)
   
        
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
                    
class Booking(models.Model):
    hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    amount = models.ForeignKey(Rooms,  on_delete=models.CASCADE)
    user =  models.ManyToManyField(Customer, related_name='bookings')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.hotels                    
    
