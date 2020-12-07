
#### REST FRAMEWORK #####

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

##### SERIALIZERS #####

from users.serializers import BuyerOrderSerializer

from items.serializers import ItemSerializer


##### MODELS #####

from django.contrib.auth.models import User
 
from users.models import BuyerOrder

from items.models import Item


############### Normalizations ##############

from utils.normalizer import normalize_text 

############## Product features ( Under Developement )

from products import products_info



class AddProductAPI(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = ItemSerializer

    #serializer_class = RegisterSerializer

    def get_object(self):

        user__ = self.request.user

        return user__

    def post(self, request, *args, **kwargs):


            item_serializer = self.get_serializer(data = request.data  )

            item_serializer.is_valid(raise_exception=True)

            item = item_serializer.save(user = self.get_object(),
                                        item_name_normalized = normalize_text(request.data["item_name"]),
                                        top_product = products_info.IsTopProduct(),
                                        featured_product = products_info.IsFeaturedProduct(),)
            res = {
            "status": 'success',
            "code": status.HTTP_200_OK,
            "message": 'Item Saved Successfully',
            "item": ItemSerializer(item, context=self.get_serializer_context()).data
            
            }

            return Response(res , status=status.HTTP_200_OK)




class GetProductsAPI(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated,]
     

    def get_user(self):

        return self.request.user

    def get(self, request, *args, **kwargs):

            user = self.get_user()

            _items = list()

            #orders_ = self.model.objects.all()

            orders = Item.objects.filter(user = user) 

            for i, obj in enumerate(orders) :
                _items.append( { 
                                        "Info" : ItemSerializer(obj).data,
                                        }
                                        )


            res = {
            "status": 'success',
            "code": status.HTTP_200_OK,
            "message": 'Fteched successfully',
            "items" : _items,
            }

            return Response(res , status=status.HTTP_200_OK)


