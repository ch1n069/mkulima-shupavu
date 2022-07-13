from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from users.models import Farmer, Buyer, Supplier, Inputs, Crop, Profile
from users.models import User 

<<<<<<< HEAD
class UserAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (None, {
    #         'fields': ("Farmer", "Supplier", "Buyer", "Inputs", "Crop")
    #     }),
        exclude = ["fieldsets"]

        
        
    
=======
# class UserAdmin(admin.ModelAdmin):
#     exclude = (
#         (None, {
#             'fields': ("Farmer", "Supplier", "Buyer", "Inputs", "Crop")
#         }),
#         ("exclude")
        
#     )


class UserAdmin(admin.ModelAdmin):
    exclude = ["fieldsets"]


>>>>>>> 554056c90502923a1d6d31a6f75a99f4f07668fe

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Farmer)
admin.site.register(Buyer)
admin.site.register(Supplier)
admin.site.register(Inputs)
admin.site.register(Crop)
admin.site.register(Profile)

# admin.site.ntregister(Age)




