from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from api.models import User, Customer, owner, Facility, Hotel, Rooms, Booking


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
   
    # admin  = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(), # Or User.objects.filter(active=True)
    #     required=False, 
    #     allow_null=True, 
    #     default=None)
    class Meta:
        model = Hotel
        fields = "__all__"
        
    # def create(self, validated_data):
    #     instance = self.Meta.model(**validated_data)
    #     instance.save()
    #     return instance
   

# Add Booking
class BookingSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Booking
        fields = "__all__"

    
# Add Rooms
class RoomSerializer(serializers.ModelSerializer):
    # hotel = serializers.SlugRelatedField(slug_field='hotel_name', read_only=True)

    class Meta:
        model = Rooms
        fields = "__all__"
