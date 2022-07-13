from django.shortcuts import get_object_or_404, render
from users.models import Farmer, Buyer, Supplier
from users.serializer import FarmerSerializer, BuyerSerializer, SupplierSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from users.serializer import * 
from users.models import User


# Create your views here.
class FarmerData(APIView):
    '''
    allow access to only authenticated users with role of farmers
    '''
    
    def get(self, request, format = None):    
        user = request.user
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
    
class SupplierData(APIView):
    '''
    allow access to suppliers only
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request, format = None):
        user = request.user
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

    # def update(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     valid = serializer.is_valid(raise_exception=True)

    #     try:
    #         if valid:
    #             serializer.save()
    #         status_code = status.HTTP_201_CREATED

    #         response = {
    #             'success': True,
    #             'statusCode': status_code,
    #             'message': 'Profile successfully created!',
    #             'user': {
    #                 'first_name': serializer.data['first_name'],
    #                'last_name': serializer.data['last_name'],
    #             #    'username' :serializer.data['username'],
    #                'contact': serializer.data['contact'],
    #                'location': serializer.data['location'],
    #             }
    #         }

    #         return Response(response, status=status_code) 
        
    #     except Profile.DoesNotExist:
    #         raise serializers.ValidationError('Profile does not exist')

    def retrieve(self, request, pk = None):
        queryset = Profile.objects.all()
        user = get_object_or_404(queryset, pk = pk)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
        


    # def get_queryset(self):
    #     if self.action == 'list':
    #         return self.queryset.filter(user=self.request.user)
    #     return self.queryset



# profile update view
# class UpdateProfileView(generics.UpdateAPIView):

#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UpdateUserSerializer

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
        
        # user = request.user
        # if user.role == 1 or user.role == 2 or user.role == 3 or user.role == 4:
        #     response = {
        #         'success': False,
        #         'status_code': status.HTTP_403_FORBIDDEN,
        #         'message': 'You are not authorized to perform this action'
        #     }
        #     return response(response, status.HTTP_403_FORBIDDEN)
        # else:
        #     users = User.objects.all()
        #     serializer = self.serializer_class(users, many=True)
        #     response = {
        #         'success': True,
        #         'status_code': status.HTTP_200_OK,
        #         'message': 'Successfully fetched users',
        #         'users': serializer.data


         

# class BuyerData(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, request, format = None):
#         buyer_data = Buyer.objects.all()
#         serializers = BuyerSerializer(buyer_data, many=True)
#         return Response(serializers.data)
#     def post(self, request, format = None):
#         serializers = BuyerSerializer(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status = status.HTTP_201_CREATED)
#         return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    
# class SupplierData(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, request, format = None):
#         supplier_data = Supplier.objects.all()
#         serializers = SupplierSerializer(supplier_data, many=True)
#         return Response(serializers.data)
#     def post(self, request, format = None):
#         serializers = SupplierSerializer(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status = status.HTTP_201_CREATED)
#         return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)    

# user profile update
class SingleProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, pk=None):
        return Profile.objects.filter(user=self.request.user.id)
        # profile = get_object_or_404(self.queryset, pk=pk)
        # serializer
