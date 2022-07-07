from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken
from users.models import Farmer, Buyer, Supplier, User
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login


# farmer class serializer
class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['user_details', 'identification_number', 'mpesa_statements', 'identification_card', 'loan_amount', 'production', 'land_size', 'revenue', 'amount_payable']
        
        
class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['user_details', 'crop_to_buy', 'bags_to_buy', 'invoice']
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['user_details', 'inputs_details', 'inputs_total', 'invoice']
        
# class AgentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Agent
#         fields = ['user_details', 'farmer_supervising', 'farmers_allocated']                
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'contact', 'location', 'role']

# # user registration and authentication
class UserRegisterSerializer(serializers.ModelSerializer):
    # username = serializers.CharField()
    # password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        
    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user
    
# user login
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    
    def create(self, validated_date):
        pass
    def update(self, instance, validated_data):
        pass
    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        
        # user.save()
        print(user)
        if user is None:
            raise serializers.ValidationError("Non existent user")
        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)
            update_last_login(None, user)
            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role,
            }
            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("User is not registered")
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = (
            'email',
            'role'
        )

