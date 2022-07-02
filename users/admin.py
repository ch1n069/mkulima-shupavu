from django.contrib import admin
from users.models import Farmer, Buyer, Supplier, Agent

# # Register your models here.
admin.site.register(Farmer)
admin.site.register(Buyer)
admin.site.register(Supplier)
admin.site.register(Agent)