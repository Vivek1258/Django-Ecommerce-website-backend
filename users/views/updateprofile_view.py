
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
 



 
class UpdateBuyerProfileAPI(generics.UpdateAPIView):

    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = BuyerProfileSerializer

    def get_object(self):

        user__ = self.request.user

        return BuyerProfile.objects.get(user = user__)

    def update(self, request, *args, **kwargs):

        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            
            self.object.mobile_number = serializer.data.get("mobile_number")
            self.object.img_link = serializer.data.get("img_link")
            self.object.lane_no = serializer.data.get("lane_no")
            self.object.landmark = serializer.data.get("landmark")
            self.object.village = serializer.data.get("village")
            self.object.state = serializer.data.get("state")
            self.object.district = serializer.data.get("district")



            self.object.save()

            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Profile updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UpdateSellerProfileAPI(generics.UpdateAPIView):

    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = SellerProfileSerializer

    def get_object(self):

        user__ = self.request.user

        return SellerProfile.objects.get(user = user__)

    def update(self, request, *args, **kwargs):

        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            
            self.object.mobile_number = serializer.data.get("mobile_number")
            self.object.img_link = serializer.data.get("img_link")

            self.object.landmark = serializer.data.get("landmark")
            self.object.village = serializer.data.get("village")
            self.object.state = serializer.data.get("state")
            self.object.district = serializer.data.get("district")

            self.object.shop_type = serializer.data.get("shop_type")
            self.object.official_doc_link = serializer.data.get("official_doc_link")
            
            
            self.object.save()

            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Profile updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


