from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Farmer, Buyer, Supplier
from users.models import User 


# Register your models here.
admin.site.register(Buyer)
admin.site.register(Supplier)

# admin.site.ntregister(Age)

