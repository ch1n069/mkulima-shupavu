from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


# custom  ABSTRACT user model
class User(AbstractUser):
    # is_farmer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    # is_agent = models.BooleanField(default=False)

    def __str__(self):
        return self.username



class Supplier(models.Model):
    '''
    supplier provides the inputs to the farmer and is paid promptly depending on the
    inputs supplied
    should see their invoice as well as all inputs supplied
    Args:
        user_details, inputs_details, inputs_total, invoice
    '''
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=False, default = '')
    contact = models.IntegerField(null=False, default = 0)
    location = models.CharField(max_length=255, null=False, default = '')
    # inputs_details = models.ForeignKey(Inputs, on_delete=models.CASCADE)
    inputs_total = models.IntegerField(null=True)
    invoice = models.DecimalField(decimal_places=2, max_digits=20)
    
    def __str__(self):      
        return str(self.invoice) 

class Buyer(models.Model):
    '''
    buyer partners with us and purchases farmer's production from our platform
    Args:
        user_details, crop_to_buy, bags_to_buy, invoice
    '''
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=False, default = '')
    contact = models.IntegerField(null=False, default = 0)
    location = models.CharField(max_length=255, null=False, default = '')
    crop_to_buy = models.CharField(max_length=255, null=False)
    bags_to_buy = models.IntegerField(null=True)
    invoice = models.DecimalField(decimal_places=2, max_digits=20)
    
    def __str__(self):      
        return str(self.invoice) 
