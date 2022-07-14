from rest_framework import serializers
from django.db import transaction

from api.models import User, Customer, owner, Facility, Hotel, Room, Booking


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username', 'email' ,'is_owner']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username', 'email', 'is_owner']

class regSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = 'email'

class CustomerSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        # 'name','contact',
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_customer=True
        user.save()
        Customer.objects.create(user=user)
        return user
    @transaction.atomic
    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            

        )
     
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_customer = True
       
        user.save() 
        customer = Customer.objects.create(user=user)
        customer.save()
        return user



class HotelAdminSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2'] # 'name',
        extra_kwargs={
            'password':{'write_only':True}
        }
    

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_owner=True
        user.save()
        owner.objects.create(user=user)
        return user




# Add Hotel
class HotelSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Hotel
        fields = "__all__"
        

# Add Booking
class BookingSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(slug_field='user', read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Booking
        fields = "__all__"

    
# Add Rooms
class RoomSerializer(serializers.ModelSerializer):
    # hotel = serializers.SlugRelatedField(slug_field='hotel_name', read_only=True)

    class Meta:
        model = Room
        fields = "__all__"
