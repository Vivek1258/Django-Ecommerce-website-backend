
#### REST FRAMEWORK #####

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

##### SERIALIZERS #####

from users.serializers import BuyerOrderSerializer

from users.serializers import SellerProfileSerializer

from items.serializers import ItemSerializer


##### MODELS #####

from django.contrib.auth.models import User
 
from users.models import BuyerOrder
from users.models import SellerProfile

from items.models import Item






################################ Orders ###############################



class PlaceOrderAPI(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated,]

    def get_user(self):

        return self.request.user

    def get_item(self):

        return Item.objects.get(id = self.request.data['item_id'])

    def post(self, request, *args, **kwargs):
 

            order_serializer = BuyerOrderSerializer(data = request.data )

 
            order_serializer.is_valid(raise_exception=True)


            user = self.get_user()
            item = self.get_item()


            order = order_serializer.save( user = user,
                                          item = item )

            ## Update the stok when the order is placed 


            item.stock = item.stock - 1

            item.save() 

            res = {
            "status": 'success',
            "code": status.HTTP_200_OK,
            "message": 'Ordered successfully',
            "order" : BuyerOrderSerializer(order).data
            }

            return Response(res , status=status.HTTP_200_OK)




class GetOrdersAPI(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated,]
     

    def get_user(self):

        return self.request.user

    def get(self, request, *args, **kwargs):

            user = self.get_user()

            ordered_items = list()

            #orders_ = self.model.objects.all()

            orders = BuyerOrder.objects.filter(user = user) 

            for i, obj in enumerate(orders) :
                order_info = obj.item

                # Every Item has info about the users(field) how posted it
                # That user info can be used to get sellerprofile

                seller_info = SellerProfile.objects.get(user = obj.item.user)


                ordered_items.append( {"placed" : obj.placed,
                                        "Order Satus"  : obj.order_sat,
                                        "Info" : ItemSerializer(order_info).data,
                                        "seller" : SellerProfileSerializer(seller_info).data
                                        }
                                        )


            res = {
            "status": 'success',
            "code": status.HTTP_200_OK,
            "message": 'Fteched successfully',
            "ordered_items" : ordered_items,
            }

            return Response(res , status=status.HTTP_200_OK)





