

from enum import unique
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import Farmer, Buyer, Supplier, User, Profile
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

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
                fields = '__all__'
                extra_kwargs = {"password": {'write_only': True}}
                fieldsets = (None)
                # exclude = ['date_joined', 'last_login']

class ProfileSerializer(serializers.ModelSerializer):
        # user  = serializers.CharField(required = True)

        class Meta:
                model = Profile
                fields = '__all__'

        
# # user registration and authentication
class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators = [UniqueValidator(queryset=User.objects.all())])
    role = serializers.ChoiceField(choices = User.ROLE_CHOICES, required = True) 
    password = serializers.CharField(required = True, validators = [validate_password])
    confirm_password  = serializers.CharField(required = True)
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'role', 'password', 'confirm_password')
        extra_kwargs = {"password": {'write_only': True}, "confirm_password": {'write_only': True}}
        
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': "Password fields did not match"})
        return attrs 
    
    def create(self, validated_data):
        auth_user = User.objects.create(**validated_data)
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
        user = User.objects.get(email=email)
        authenticate(user)
        
        user.save()
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

