from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import *

# Register your models here.
admin.site.register(Buyer)
admin.site.register(Supplier)
admin.site.register(User, UserAdmin)
admin.site.register(Farmer)
admin.site.register(Agent)

