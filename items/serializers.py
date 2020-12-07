from rest_framework import serializers 
from items.models import Item
  
   
class ItemSerializer(serializers.ModelSerializer):

	class Meta:
	    model = Item
	    fields = (
	    		  'id',

	              'item_name',
	              'image_link',
	              'availability',
	              'rating',
	              'price',

	              'description',
	              'specifiation',

	              'top_product',
	              'featured_product',

	              'item_name_normalized',
	              'item_type',
	              'item_sub_type',

	              'stock',
	              
	              ) 