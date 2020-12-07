from django.shortcuts import render
  
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework import generics
from rest_framework import permissions

from rest_framework.response import Response

  
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view, renderer_classes


from utils.normalizer import normalize_text 

from products import products_info

######## CLASS based view for CURD operations in items  ##########

class Items(generics.GenericAPIView):

    # Add excess control 

    serializer_class = ItemSerializer
    model = Item


    # Add Item to the DB  
    def post(self, request, *args, **kwargs):

        item_serializer = self.get_serializer(data=request.data)

        if item_serializer.is_valid():
            item__ = item_serializer.save(
                                        item_name_normalized = normalize_text(request.data["item_name"]),
                                        top_product = products_info.IsTopProduct(),
                                        featured_product = products_info.IsFeaturedProduct(),)
            return JsonResponse(item_serializer.data, status=status.HTTP_201_CREATED) 

        return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    # Get the list of items from the DB, based on item name 
    def get(self, request, *args, **kwargs):

        items_ = self.model.objects.all()
        
        name = request.GET.get('item_name', None)

        print(request.GET)

        if name is not None:
            items_ = items_.filter(item_name__contains=name)
            # try 
        
        items_serializer = self.get_serializer(items_, many=True)
        return JsonResponse(items_serializer.data, safe=False)



    # Update the item details by ID 
    def put(self, request ):
        try: 
            item_instance = self.model.objects.get(pk=request.data['id']) 
        except  Item.DoesNotExist: 
            return JsonResponse({'message': 'This Item does not exist'},
                                 status=status.HTTP_404_NOT_FOUND) 

        item_serializer = self.get_serializer(item_instance ,data=request.data)

        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse(item_serializer.data, status=status.HTTP_201_CREATED) 

        return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # Delete the item by ID 
    def delete(self, request):

        try: 
            item_instance = self.model.objects.get(pk=request.data['id']) 
        except  Item.DoesNotExist: 
            return JsonResponse({'message': 'This Item does not exist'},
                                 status=status.HTTP_404_NOT_FOUND) 
        item_instance.delete()

        response = { 'message': 'Item deleted successfully'}

        return JsonResponse(response , status=status.HTTP_200_OK )



############################ Function Based View #####################


#get all avalable items 
@api_view(['GET'])
def item_list_available(request):
    items = Item.objects.filter(availability=True)
        
    if request.method == 'GET': 
        items_serializer =  ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)

#get top items 
@api_view(['GET'])
def get_top_products(request):
    items = Item.objects.filter(top_product = True)
        
    if request.method == 'GET': 
        items_serializer =  ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)


#get featured items 
@api_view(['GET'])
def get_featured_products(request):
    items = Item.objects.filter(featured_product=True)
        
    if request.method == 'GET': 
        op_product=True
        items_serializer =  ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)
