from django.shortcuts import get_object_or_404, render
from users.models import Farmer, Buyer, Supplier, Stock, Loan, Profile
from users.serializer import FarmerSerializer, BuyerSerializer, SupplierSerializer, ProfileSerializer, GuarantorSerializer, InputsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from users.serializer import * 
from users.models import User


# Create your views here.
class FarmerData(APIView):
    '''
    allow access to only authenticated users with role of farmers
    '''
    
    def get(self, request, format = None):    
        user = request.user
        print(user.role)
        if user.role == 1: 
                                     
            farmer_data = Farmer.objects.all()
            serializers = FarmerSerializer(farmer_data, many=True)
            return Response(serializers.data)
        else:
            status_code = status.HTTP_401_UNAUTHORIZED
            response = {
                'statusCode': status_code,
                'message': "User not authorized to perform this action"
            }
        return Response(response)
    
    def post(self, request, format = None):
        serializers = FarmerSerializer(data = request.data)
        user = request.user
        if serializers.is_valid() and user.role == 1:
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class BuyerData(APIView):
    '''
    allow access to only authenticated users with role of buyers
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request, format = None):
        user = request.user
        if user.role == 2: 
            buyer_data = Buyer.objects.all()
            serializers = BuyerSerializer(buyer_data, many=True)
            return Response(serializers.data)
        else:
            status_code = status.HTTP_401_UNAUTHORIZED
            response = {
                'statusCode': status_code,
                'message': "User not authorized to perform this action"
            }
        return Response(response)
    
    def post(self, request, format = None):
        user = request.user
        serializers = BuyerSerializer(data = request.data)
        if serializers.is_valid() and user.role == 2:
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)        
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # needs to be worked on !!
class SupplierData(APIView):
    '''
    allow access to suppliers only
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request, format = None):
        user = request.user
        print(user.role)
        if user.role == 4: 
            supplier_data = Supplier.objects.all()
            serializers = SupplierSerializer(supplier_data, many=True)
            return Response(serializers.data)
        else:
            status_code = status.HTTP_401_UNAUTHORIZED
            response = {
                'statusCode': status_code,
                'message': "User not authorized to perform this action"
            }
        return Response(response)
    
    def post(self, request, format = None):
        serializers = SupplierSerializer(data = request.data)
        user = request.user

        if serializers.is_valid() and user.role == 4:
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)    
 
class AuthUserRegistrationView(APIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': {
                    'first_name': serializer.data['first_name'],
                   'last_name': serializer.data['last_name'],
                   'username' :serializer.data['username'],
                   'email': serializer.data['email'],
                   'role': serializer.data['role'],
                }
            }

        return Response(response, status=status_code) 

class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        # data = request.data
        # print(data)
        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

        return Response(response, status=status_code)

# user profile view
class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Profile successfully created!',
                'user': {
                    'first_name': serializer.data['first_name'],
                   'last_name': serializer.data['last_name'],
                #    'username' :serializer.data['username'],
                   'contact': serializer.data['contact'],
                   'location': serializer.data['location'],
                }
            }

            return Response(response, status=status_code) 

  
    def retrieve(self, request, pk = None):
        queryset = Profile.objects.all()
        user = get_object_or_404(queryset, pk = pk)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
        

# user profile update
class SingleProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, pk=None):
        return Profile.objects.filter(user=self.request.user.id)
        # profile = get_object_or_404(self.queryset, pk=pk)
        # serializer




class UserListView(viewsets.ModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    # allow admin only
    permission_classes = (permissions.IsAdminUser,)

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserListSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk = pk)
        serializer = UserListSerializer(user)
        return Response(serializer.data)

# # user profile view
# class ProfileView(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ProfileSerializer

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)
#         if valid:
#             serializer.save()
#             status_code = status.HTTP_201_CREATED
#             response = {
#                 'success': True,
#                 'statusCode': status_code,
#                 'message': 'Profile successfully created!',
#                 'user': {
#                     'first_name': serializer.data['first_name'],
#                    'last_name': serializer.data['last_name'],
#                 #    'username' :serializer.data['username'],
#                    'contact': serializer.data['contact'],
#                    'location': serializer.data['location'],
#                 }
#             }
#         return Response(response, status=status_code)

#     def retrieve(self, request, pk = None):
#         queryset = Profile.objects.all()
#         user = get_object_or_404(queryset, pk = pk)
#         serializer = ProfileSerializer(user)
#         return Response(serializer.data)
    
    # user profile update
# class SingleProfileView(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

#     def get(self, pk=None):
#         return Profile.objects.filter(user=self.request.user.id)
#         # profile = get_object_or_404(self.queryset, pk=pk)
@authentication_classes([]) 
@permission_classes([])     
class LoanView(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


    # permission_classes = (IsAuthenticated)
    
    # permission_classes = [IsAuthenticated]

    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=False)
        if valid:   
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Details submitted successfully, pending approval',
                'user': {
                    'first_name': serializer.data['first_name'],
                    'last_name': serializer.data['last_name'],
                    'id_number' :serializer.data['id_number'],
                    'location': serializer.data['location'],

                    # 'gender': serializer.data['gender'],
                    'crop': serializer.data['crop'],
                    # 'email': serializer.data['email'],
                }
                
            }
        return Response(response, status=status_code)
    
        
    # def list(self, request, location):
    #     user = request.user
    #     if user:
    #         supplier_location = Supplier.objects.get(location = location)
    #         loans_location = Loan.objects.get(supplier_location = supplier_location)
    #         return Response(loans_location)
    #     else:
    #         response = {
    #             "message": "Cannot access action",
    #             "status_code": status.HTTP_400_BAD_REQUEST
    #             }
    #         return Response(response)
       
    
class GuarantorView(APIView):
    def get(self, request):
        serializer_class = GuarantorSerializer
        queryset = Guarantor.objects.all()
        permission_classes = (permissions.IsAdminUser,)
        return Response (queryset)

class InputsView(viewsets.ModelViewSet):
    def create(self, request):
        query = Inputs.objects.all()
        # serializer_class = InputsSerializer
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        
        user = request.user        
        if user.role == 1 and valid():
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Farm Inputs recorded,loan pending approval',
                'user': {
                    'fertilizer_name': serializer.data['fertilizer_name'],
                    'chemical_name': serializer.data['chemical_name'],
                    'seed_name' :serializer.data['seed_name'],
                    'fertilizer_bags': serializer.data['fertilizer_bags'],
                    'seed_quantity': serializer.data['seed_quantity'],
                    'chemicals': serializer.data['chemicals'],
                }                
            }
        return Response(response, status=status_code)
            
            
    
    def list(self, request):
        serializer_class = InputsSerializer
        queryset = Inputs.objects.all()
        permission_classes = (permissions.IsAdminUser,)
        return Response (queryset)   
    
    
    
    
    
    
    
     
      



# user profile update
class SingleProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, pk=None):
        return Profile.objects.filter(user=self.request.user.id)
        # profile = get_object_or_404(self.queryset, pk=pk)
        # serializer


