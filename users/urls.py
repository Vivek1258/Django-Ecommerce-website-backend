  
from knox import views as knox_views

####### General ##########
from .views import LoginAPI
from .views import UserAPI
from .views import ChangePasswordView

####### Buyer ##########
from .views import BuyerRegisterAPI
from .views import BuyerProfileAPI
from .views import UpdateBuyerProfileAPI


####### Seller ##########
from .views import SellerProfileAPI
from .views import SellerRegisterAPI
from .views import UpdateSellerProfileAPI


######## Oredring ##########

from .views import PlaceOrderAPI
from .views import GetOrdersAPI

########## Adding Items/Products to the DB by seller 

from .views import AddProductAPI
from .views import GetProductsAPI


from django.urls import path
 
urlpatterns = [

    path('api/register_buyer/', BuyerRegisterAPI.as_view(), name='register_buyer'),
    path('api/buyer-profile/', BuyerProfileAPI.as_view(), name='buyer-profile'),
    path('api/update-buyer-profile/', UpdateBuyerProfileAPI.as_view(), name='update-buyer-profile'),

    path('api/register_seller/', SellerRegisterAPI.as_view(), name='register_seller'),
    path('api/seller-profile/', SellerProfileAPI.as_view(), name='seller-profile'),
    path('api/update-seller-profile/', UpdateSellerProfileAPI.as_view(), name='update-seller-profile'),

    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),


    path('api/user/', UserAPI.as_view(), name='user'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),


    path('api/place_order/' , PlaceOrderAPI.as_view() , name = "place order"),
    path('api/get_orders/' , GetOrdersAPI.as_view() , name = "get orders"),


    path('api/add_product/' , AddProductAPI.as_view() , name = "add product"),
    path('api/get_products/' , GetProductsAPI.as_view() , name = "get products"),

    # ADD :--> path : api/reset-password/   ( with email verification)
] 

 