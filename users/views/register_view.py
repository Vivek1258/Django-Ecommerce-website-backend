###### IMPORTS 

 
##### RESTFRAMEWORK ######

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response


##### SERIALIZERS ######

from users.serializers import RegisterSerializer
from users.serializers import UserSerializer
from users.serializers import BuyerProfileSerializer
from users.serializers import SellerProfileSerializer

##### MODELS #####

from knox.models import AuthToken

class BuyerRegisterAPI(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):

            user_serializer = RegisterSerializer(data=request.data)
            profile_serializer = BuyerProfileSerializer(data = request.data  )

            user_serializer.is_valid(raise_exception=True)
            profile_serializer.is_valid(raise_exception=True)

            user = user_serializer.save()

            profile = profile_serializer.save( user = user )

            res = {
            "status": 'success',
            "code": status.HTTP_200_OK,
            "message": 'User registerd successfully',
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "user_profile" : SellerProfileSerializer(profile ,context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
            }

            return Response(res , status=status.HTTP_200_OK)


class SellerRegisterAPI(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):

            user_serializer = RegisterSerializer(data=request.data)
            profile_serializer = SellerProfileSerializer(data = request.data  )

            user_serializer.is_valid(raise_exception=True)
            profile_serializer.is_valid(raise_exception=True)

            user = user_serializer.save()

            profile = profile_serializer.save( user = user )

            res = {
            "status": 'success',
            "code": status.HTTP_200_OK,
            "message": 'User registerd successfully',
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "user_profile" : SellerProfileSerializer(profile ,context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
            }

            return Response(res , status=status.HTTP_200_OK)



