from rest_framework import serializers
from users.models import Farmer, Buyer, Supplier, Agent

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
        fields = ['user_details', 'username','contact','location','farmer_supervising', 'farmers_allocated', 'inputs_record']                