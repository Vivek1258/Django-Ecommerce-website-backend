from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

from django.contrib.auth.models import User



############################### SELLER ####################


class SellerProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add = True)

    mobile_number = models.BigIntegerField( blank = True )

    img_link = models.URLField(max_length=5000,
                               blank=True, # image of a user can be ocptional 
                               default = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png" )

    #address = models.TextField(max_length=1000, blank=True ) # address of a user can be ocptional 
                                                             #while regiestering he/she can fill it when he is making an order 


    shop_type = models.TextField(max_length=1000, blank=True )
    

    # Official Doc for the shop owenrship 
    
    official_doc_link = models.URLField(max_length=5000,
                               blank=True 
                             )
                                                  
                                                           
    lane_no = models.TextField(max_length=50, blank=True )
    
    landmark = models.TextField(max_length=1000, blank=True )

    village = models.TextField(max_length=100, blank=True ) 

    district = models.TextField(max_length=100, blank=True )

    state = models.TextField(max_length=100, blank=True )



    def __str__(self):
        return self.user.username



######################### BUYER ##############################

class BuyerProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add = True)

    mobile_number = models.BigIntegerField( blank = False )

    img_link = models.URLField(max_length=5000,
                               blank=True, # image of a user can be ocptional 
                               default = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png" )

    #address = models.TextField(max_length=1000, blank=True ) # address of a user can be ocptional 
                                                             #while regiestering he/she can fill it when he is making an order 

    lane_no = models.TextField(max_length=50, blank=True )
    
    landmark = models.TextField(max_length=1000, blank=True )

    village = models.TextField(max_length=100, blank=True ) 

    district = models.TextField(max_length=100, blank=True )

    state = models.TextField(max_length=100, blank=True )

    pro_user = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username



from items.models import Item

class BuyerOrder(models.Model):

    user = models.ForeignKey( User, on_delete=models.CASCADE)

    item = models.ForeignKey( Item, on_delete=models.CASCADE)

    #order_id = models.IntegerField( blank = False )
    placed = models.DateTimeField(auto_now_add = True)

    order_sat = models.TextField(max_length=1000, blank=False )

    def __str__(self):
        return self.id


### Extra addition 
"""

class UserCart(models.Model):

    user = models.ForeignKey( User, on_delete=models.CASCADE)

    item = models.ForeignKey( Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




"""

################################## UNDER DEVELOPEMENT PART ###########################

# Reset password with email verification 

## CURRENT status:

        # If user is logged in then he can directly update password 
        # If user forgets the password then vo gaya kuki koi aur ocption nahi hai, we need to work on 
        # this part 

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "spareware20@gmail.com",
        # to:
        [reset_password_token.user.email]
    )