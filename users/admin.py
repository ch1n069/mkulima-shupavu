from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from users.models import Farmer, Buyer, Supplier, Inputs, Crop, Profile
from users.models import User 

# class UserAdmin(admin.ModelAdmin):
#     exclude = (
#         (None, {
#             'fields': ("Farmer", "Supplier", "Buyer", "Inputs", "Crop")
#         }),
#         ("exclude")
        
#     )


class UserAdmin(admin.ModelAdmin):
    exclude = ["fieldsets"]


class FarmerAdmin(admin.ModelAdmin):
    list_display = ['inputs_picked','loan_amount','production','land_size','revenue','amount_payable']
    list_filter = ['land_size']
    search_fields = ['user_details']
    prepopulated_fields ={'slug':['loan_amount']}
    actions = ('set_farmer_published')

    # set up admin actions
    def set_farmer_published(self,request,queryset):
        queryset.update(amount_payable=False)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user_details','inputs_total','invoice']

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Farmer,FarmerAdmin)
admin.site.register(Buyer,)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Inputs)
admin.site.register(Crop)
admin.site.register(Profile)

# admin.site.ntregister(Age)




