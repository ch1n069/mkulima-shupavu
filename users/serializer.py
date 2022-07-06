from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from .models import Supplier, Buyer

class SupplierCustomRegistrationSerializer(RegisterSerializer):
    user_detail = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    username = serializers.CharField(required=True)
    contact = serializers.CharField(required=True)
    location = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(SupplierCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'username' : self.validated_data.get('username', ''),
                'contact' : self.validated_data.get('contact', ''),
                'location': self.validated_data.get('location', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(SupplierCustomRegistrationSerializer, self).save(request)
        user.is_seller = True
        user.save()
        supplier = Supplier(seller=user, location=self.cleaned_data.get('location'), 
                username=self.cleaned_data.get('username'),
                contact=self.cleaned_data.get('contact'))
        supplier.save()
        return user


class BuyerCustomRegistrationSerializer(RegisterSerializer):
    user_detail = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    username = serializers.CharField(required=True)
    contact = serializers.CharField(required=True)
    location = serializers.CharField(required=True)
    crop_to_buy = serializers.CharField(required=True)
    bags_to_buy = serializers.CharField(required=True)
 

    def get_cleaned_data(self):
            data = super(BuyerCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'username' : self.validated_data.get('username', ''),
                'contact' : self.validated_data.get('contact', ''),
                'location' : self.validated_data.get('location', ''),
                'crop_to_buy' : self.validated_data.get('crop_to_buy', ''),
                'bags_to_buy' : self.validated_data.get('bags_to_buy', ''),
           
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(BuyerCustomRegistrationSerializer, self).save(request)
        user.is_buyer = True
        user.save()
        buyer = Buyer(buyer=user,country=self.cleaned_data.get('location'),
                username=self.cleaned_data.get('username'),
                contact=self.cleaned_data.get('contact'),
                crop_to_buy=self.cleaned_data.get('crop_to_buy'),
                bags_to_buy=self.cleaned_data.get('bags_to_buy'))
        buyer.save()
        return user