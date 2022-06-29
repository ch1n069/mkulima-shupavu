from django.contrib import admin
from .models import Input,Plant,Land,Garanter,Profile,ModuleSubscribe,Agents

# Register your models here.
admin.site.register(Input)
admin.site.register(ModuleSubscribe)
admin.site.register(Plant)
admin.site.register(Land)
admin.site.register(Garanter)
admin.site.register(Profile)
admin.site.register(Agents)