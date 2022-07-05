from django.contrib import admin
from users.models import Farmer, Buyer, Supplier, Agent
from django.utils import timezone

# # Register your models here.
class FarmerAdmin(admin.ModelAdmin):
    display = ('user_details','username','contact')
    search_fields = ['username']

class BuyerAdmin(admin.ModelAdmin):
    display = ('user_details','username','contact','crop_to_buy')
    search_fields = ['username']

class SupplierAdmin(admin.ModelAdmin):
    display = ('user_details','username','contact','inputs_details','inputs_total')
    search_fields = ['username']

class AgentAdmin(admin.ModelAdmin):
    display = ('user_details','username','contact','location','farmer_supervising','farmers_allocated')
    search_fields = ['username']
    prepopulated_fields = {'slug':['username']}
    actions = ('set_published')

    def days_since_creation(self,Agent):
        diff = timezone.now() - Agent.date_created
        return diff.days
    days_since_creation.short_description = 'Days Active'



    def set_published(self,request,queryset):
        count = queryset.update(username=False)
        self.message_user(request, '{} The selected have been saved successfully'.format(count))

admin.site.register(Farmer,FarmerAdmin)
admin.site.register(Buyer,BuyerAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Agent,AgentAdmin)