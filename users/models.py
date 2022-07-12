from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# # custom  ABSTRACT user model
# class User(AbstractUser):
#     # is_farmer = models.BooleanField(default=False)
#     is_supplier = models.BooleanField(default=False)
#     is_buyer = models.BooleanField(default=False)
  

#     def __str__(self):
#         return self.username



# class Supplier(models.Model):
#     '''
#     supplier provides the inputs to the farmer and is paid promptly depending on the
#     inputs supplied
#     should see their invoice as well as all inputs supplied
#     Args:
#         user_details, inputs_details, inputs_total, invoice
#     '''
#     user_details = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     username = models.CharField(max_length=255, null=False, default = '')
#     contact = models.BigIntegerField (null=False, default = 0)
#     location = models.CharField(max_length=255, null=False, default = '')
#     # inputs_details = models.ForeignKey(Inputs, on_delete=models.CASCADE)
#     inputs_total = models.BigIntegerField (null=True)
#     invoice = models.DecimalField(decimal_places=2, max_digits=20,blank=True,null=True)
    
#     def __str__(self):      
#         return str(self.username) 

# class Buyer(models.Model):
#     '''
#     buyer partners with us and purchases farmer's production from our platform
#     Args:
#         user_details, crop_to_buy, bags_to_buy, invoice
#     '''
#     user_details = models.OneToOneField(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=255, null=False, default = '')
#     contact = models.BigIntegerField (null=False, default = 0)
#     location = models.CharField(max_length=255, null=False, default = '')
#     crop_to_buy = models.CharField(max_length=255, null=False)
#     bags_to_buy = models.BigIntegerField (null=True)
#     invoice = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    
#     def __str__(self):      
#         return str(self.username) 


# class Profile(models.Model):

#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     first_name = models.CharField(max_length=120, blank=False)
#     last_name = models.CharField(max_length=120, blank=False)
#     contact = models.BigIntegerField (null=False, default = 0)
#     location = models.CharField(max_length=255, null=False, default = '')
#     avatar = models.ImageField()

#     def __unicode__(self):
#         return u'Profile of user: {0}'.format(self.user.email)


# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# post_save.connect(create_profile, sender=User)


# def delete_user(sender, instance=None, **kwargs):
#     try:
#         instance.user
#     except User.DoesNotExist:
#         pass
#     else:
#         instance.user.delete()
# post_delete.connect(delete_user, sender=Profile)