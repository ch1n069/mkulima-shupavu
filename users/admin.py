from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Farmer, Buyer, Supplier, Inputs, Crop
from users.models import User 

class UserAdmin(admin.ModelAdmin):
    exclude = (
        (None, {
            'fields': ("Farmer", "Supplier", "Buyer", "Inputs", "Crop")
        }),
        ("exclude")
        
    )

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Farmer)
admin.site.register(Buyer)
admin.site.register(Supplier)
admin.site.register(Inputs)
admin.site.register(Crop)

# admin.site.ntregister(Age)

