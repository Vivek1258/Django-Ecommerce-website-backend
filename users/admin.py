from django.contrib import admin

# Register your models here.

from .models import BuyerProfile
from .models import SellerProfile


admin.site.register(BuyerProfile)
admin.site.register(SellerProfile)
