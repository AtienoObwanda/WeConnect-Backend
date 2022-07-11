from django.db import models
from django.contrib.auth.models import User, AbstractUser



class Hotel (models.Model):
    hotel_name = models.CharField(max_length=100)
    description = models.TextField(blank= True)
    tagline = models.CharField(max_length=100)
    facility1 = models.CharField(max_length=30, blank=True, null=True)
    facility2 = models.CharField(max_length=30, blank=True, null=True)
    facility3 = models.CharField(max_length=30, blank=True, null=True)
    facility4 = models.CharField(max_length=30, blank=True, null=True)
    facility5= models.CharField(max_length=30, blank=True, null=True)
    cover_image = models.ImageField(upload_to='images/')
    def __str__(self):
            return self.hotel_name

class Room (models.Model):
    ROOM_TYPE = (
        ('Standard', 'Standard'),
        ('Standard Twin', 'Standard Twin'),
        ('Deluxe', 'Deluxe'),
        ('Deluxe Twin', 'Deluxe Twin')
        )
    name = models.CharField(max_length=30, choices=ROOM_TYPE)
    tagline = models.CharField(max_length=100)
    rate = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    hotel= models.ForeignKey(Hotel,  on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    def create_room(self):
        self.save

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    amount = models.ForeignKey(Room,  on_delete=models.CASCADE)
    user =  models.ManyToManyField(User, related_name='bookings')
    date = models.DateTimeField(auto_now_add=True)
    phone = models.IntegerField(blank=True, null=True)
    check_in= models.DateTimeField()
    check_out = models.DateTimeField()
    
    def __str__(self):
        return f'{self.date}'           
    