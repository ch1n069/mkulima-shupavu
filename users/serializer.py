
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import Authenticate
from django.contrib.auth.models import update_last_login

from .models import Supplier, Buyer, User 


# class SupplierCustomRegistrationSerializer(RegisterSerializer):
#     user_detail = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
#     username = serializers.CharField(required=True)
#     # contact = serializers.CharField(required=True)
#     # location = serializers.CharField(required=True)
    
#     def get_cleaned_data(self):
#             data = super(SupplierCustomRegistrationSerializer, self).get_cleaned_data()
#             extra_data = {
#                 'username' : self.validated_data.get('username', ''),
#                 # 'contact' : self.validated_data.get('contact', ''),
#                 # 'location': self.validated_data.get('location', ''),
#             }
#             data.update(extra_data)
#             return data

#     def save(self, request):
#         user = super(SupplierCustomRegistrationSerializer, self).save(request)
#         user.is_supplier = True
#         user.save()
#         supplier = Supplier(user_details=user, location=self.cleaned_data.get('location'), 
#                 username=self.cleaned_data.get('username'),
#                 contact=self.cleaned_data.get('contact'))
#         supplier.save()
#         return user


# class BuyerCustomRegistrationSerializer(RegisterSerializer):
#     user_detail = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
#     username = serializers.CharField(required=True)
#     contact = serializers.CharField(required=True)
#     location = serializers.CharField(required=True)
#     crop_to_buy = serializers.CharField(required=True)
#     bags_to_buy = serializers.CharField(required=True)
 

#     def get_cleaned_data(self):
#             data = super(BuyerCustomRegistrationSerializer, self).get_cleaned_data()
#             extra_data = {
#                 'username' : self.validated_data.get('username', ''),
#                 'contact' : self.validated_data.get('contact', ''),
#                 'location' : self.validated_data.get('location', ''),
#                 'crop_to_buy' : self.validated_data.get('crop_to_buy', ''),
#                 'bags_to_buy' : self.validated_data.get('bags_to_buy', ''),
           
#             }
#             data.update(extra_data)
#             return data

#     def save(self, request):
#         user = super(BuyerCustomRegistrationSerializer, self).save(request)
#         user.is_buyer = True
#         user.save()
#         buyer = Buyer(user_details=user,location=self.cleaned_data.get('location'),
#                 username=self.cleaned_data.get('username'),
#                 contact=self.cleaned_data.get('contact'),
#                 crop_to_buy=self.cleaned_data.get('crop_to_buy'),
#                 bags_to_buy=self.cleaned_data.get('bags_to_buy'))
#         buyer.save()
#         return user


# # login user-seller,buyer and farmer
# # class UserLoginSerializer(serializers.Serializer):

# #         email = serializers.CharField(max_length=255)
# #         password = serializers.CharField(max_length=100, write_only=True)
# #         token = serializers.CharField(max_length=255)

# #         def validate(self,data):
# #                 email = data.get('email', None)
# #                 password = data.get('password', None)
# #                 user = Authenticate(email=email, password=password)
# #                 if user is None:
# #                         raise serializers.ValidationError('A user with this email and password is not found')

# #                 try:
# #                         update_last_login(None, user)

# #                 except User.DoesNotExist:
# #                         raise serializers.ValidationError('A user with this email and password does not exist')

# #                 return{
# #                         'email': user.email,
# #                         'token': Token,
# #                 }