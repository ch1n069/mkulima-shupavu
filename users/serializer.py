from rest_framework import serializers

from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from users.models import *


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
                username=self.cleaned_data.get('contact'),
                username=self.cleaned_data.get('crop_to_buy'),
                contact=self.cleaned_data.get('bags_to_buy'))
        buyer.save()
        return user


# farmer class serializer
class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['user_details', 'username', 'contact', 'location', 'identification_number', 'mpesa_statements', 'identification_card', 'loan_amount', 'production', 'land_size', 'revenue', 'amount_payable']
        
        
class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['user_details', 'crop_to_buy', 'bags_to_buy', 'invoice']
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['user_details', 'inputs_details', 'inputs_total', 'invoice']
        
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['user_details', 'farmer_supervising', 'farmers_allocated']                

