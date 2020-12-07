from rest_framework import generics, permissions
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BuyerProfile , SellerProfile 

from .models import BuyerOrder
 
# User Serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name' , 'last_name' , 'email' , "is_staff" , "is_superuser" ) 

        # DONE :
        #ADD "is_staff", meta : Boolean. Designates whether this user can access the admin site.
        # reference : https://docs.djangoproject.com/en/3.1/ref/contrib/auth/

class BuyerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerProfile
        fields = ('mobile_number',
                  'img_link', 
                  'pro_user',
                  'lane_no',
                  'landmark',
                  'village',
                  'district',
                  'state'
                   )


class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = ('mobile_number',
                 'img_link',  
                  'lane_no',
                  'landmark',
                  'village',
                  'district',
                  'state',
                  'shop_type',
                  'official_doc_link', )


class BuyerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerOrder
        fields = ('id', 'order_sat')#, 'orderStatus')


"""class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCart
        fields = ('mobile_number', 'img_link', 'address' , 'pro_user' )"""


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name' , 'password' , 'last_name' , 'email' , "is_staff" , "is_superuser" ) 
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
                                        validated_data['username'],
                                        first_name=validated_data['first_name'],
                                        last_name= validated_data['last_name'],
                                        email=validated_data['email'],
                                        password= validated_data['password']
                                    ) 
        return user

# Change Password

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)