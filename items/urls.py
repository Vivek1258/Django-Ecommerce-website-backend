from django.conf.urls import url 
 
from django.urls import path

from . import views as v
from .views import Items


urlpatterns = [ 

	# Under Developement 

	##### CURD operations on items DB 

    path('items_CURD/', Items.as_view() , name='Item-Operations'),
    

    ##### Filter the items based on features 

    path('available/', v.item_list_available),
    path('get-top-products/', v.get_top_products ), 
    path('get-featured-products/', v.get_featured_products),

]

