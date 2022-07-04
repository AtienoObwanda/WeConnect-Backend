from rest_framework import serializers

from api.models import User, Customer, owner, Facility, Hotel, Rooms, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'is_owner']

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

# Add Facility
class FacilitySerializer(serializers.ModelSerializer):
     class Meta:
        model = Facility
        fields = "__all__"

        def create(self, validated_data):
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance

# Add Rooms
class RoomSerializer(serializers.ModelSerializer):
     class Meta:
        model = Rooms
        fields = "__all__"

        def create(self, validated_data):
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance
# Add Hotel
class FacSerializer(serializers.ModelSerializer):
   
        class Meta:
            model = Facility
            fields = "__all__"

class HotelSerializer(serializers.ModelSerializer):
   
    admin  = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), # Or User.objects.filter(active=True)
        required=False, 
        allow_null=True, 
        default=None)
    
    # facility = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Facility.objects.all())
    Hfacilities = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='facility-detail')
    class Meta:
        model = Hotel
        fields = "__all__"

    # def create(self, validated_data):
    #     facs = validated_data.pop('facility')
    #     hotel = Hotel.objects.create(**validated_data)
    #     for fac in facs:
    #         Hotel.objects.create(user=hotel,**fac)
    #     return hotel

    

    # class Meta:
    #         model = Hotel
    #         fields = ('hotel_name','description', 'facility','cover_image', 'admin'
    #         )
    

    # def create(self, validated_data):
            
    #         instance = self.Meta.model(**validated_data)
    #         instance.save()
    #         return instance

# Add Booking
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

        def create(self, validated_data):
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance
    