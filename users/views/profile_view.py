
#### REST FRAMEWORK #####

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

##### SERIALIZERS #####

from users.serializers import UserSerializer 
from users.serializers import BuyerProfileSerializer
from users.serializers import SellerProfileSerializer


##### MODELS #####

from django.contrib.auth.models import User
 
from users.models import BuyerProfile
from users.models import SellerProfile
 


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class BuyerProfileAPI(generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticated,]
    serializer_class =  BuyerProfileSerializer

    def get_object(self):

        user__ = self.request.user

        return BuyerProfile.objects.get(user = user__)



class SellerProfileAPI(generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticated,]
    serializer_class =  SellerProfileSerializer

    def get_object(self):

        user__ = self.request.user

        return SellerProfile.objects.get(user = user__)




