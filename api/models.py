from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


    # user = models.OneToOneField(User, related_name='tutor', on_delete = models.CASCADE, primary_key = True)
    # def __str__(self):
    #         return self.user.first_name

    

class Rooms (models.Model):
    name = models.CharField(max_length=100)
    # rate = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    # hotel = models.ForeignKey(Hotel,  on_delete=models.CASCADE)
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
    # admin = models.CharField(Admin, on_delete=models.CASCADE)
   
        
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
    # user =  models.ForeignKey(Customer,  on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.hotels                    
    
