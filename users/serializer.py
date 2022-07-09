from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import Farmer, Buyer, Supplier, User
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

# farmer class serializer
class FarmerSerializer(serializers.HyperlinkedModelSerializer):
    # hyperlinkedmodelserializer works like modelserializer but returns url instead of pk
    # by default it includes a url field
    url = serializers.HyperlinkedIdentityField(view_name='farmer')
    
    class Meta:
        model = Farmer
        fields = ['url', 'user_details', 'identification_number', 'mpesa_statements', 'identification_card',
                 'land_size']
        read_only_fields = ['loan_amount', 'production', 'revenue', 'amount_payable']
        
        
class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['user_details', 'crop_to_buy', 'bags_to_buy']
        read_only_fields = ['invoice']
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        # The value source='*' has a special meaning, and is used to indicate that the entire object should be passed through
        # to the field. This can be useful for creating nested representations, or for fields which require access 
        # to the complete object in order to determine the output representation.
        supplier_details = serializers.CharField(source = '*')
        fields = ['user_details', 'inputs_details']
        read_only_fields = ['invoice', 'inputs_total']
        
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
        fields = ('first_name', 'last_name', 'username', 'email', 'role', 'password')
        extra_kwargs = {"password": {'write_only': True}}
        
    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        auth_user.set_password(validated_data['password'])
        auth_user.save()
        return auth_user
    
# user login
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
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