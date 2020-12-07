from django.db import models
  
from django.contrib.auth.models import User

class Item(models.Model):

    added = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey( User, on_delete=models.CASCADE)

    ####### Display Data  ########

    item_name = models.CharField(max_length=100, blank=False )

    image_link = models.URLField(max_length=200, blank=True ) # add default image link 

    #image = models.ImageField(upload_to="items_images/", height_field=250, width_field=250, max_length=100)

    availability = models.BooleanField(default=True)

    stock = models.IntegerField(blank=False) 

    rating = models.IntegerField(blank=True , default = 3.5 ) # Update Rating field 

    price = models.IntegerField(blank=False) 


    ########### 

    description = models.TextField(max_length=1000, blank=True )  # DESCRIPTION can be ocptional 
    
    specifiation = models.TextField(max_length=1000, blank=True )  # SPECIFICATION can be ocptional 



    ####### Extra Important Information   ########

    # for getting Product List 

    top_product = models.BooleanField(default=False,  blank=True )

    featured_product = models.BooleanField(default=False ,  blank=True )

    # for Querry parsing & recommender syatem (Update Required)

    item_name_normalized = models.CharField(max_length=100, blank= True)

    item_type = models.CharField(max_length=100, blank=False, default= "Some Item")

    item_sub_type = models.CharField(max_length=100, blank=True) 

    # Seller Information  

    #### SKIPPED because this info can be extracted by User object above 

    #seller = models.CharField(max_length=200, blank=True )

    #seller_email = models.EmailField(max_length=254, blank=True)

    #seller_mobile = models.BigIntegerField(blank=True)

    class Meta:
        ordering = ['added']


# Reference: https://docs.djangoproject.com/en/3.1/ref/models/fields/
# NOTE: Use seperate endpoints for uploading images 
# 		see ref: https://stackoverflow.com/questions/45564130/django-rest-framework-image-upload
