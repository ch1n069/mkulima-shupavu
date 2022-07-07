
from django.http import HttpResponse
from django.shortcuts import render

from users.models import Farmer, Buyer, Supplier
from users.serializer import FarmerSerializer, BuyerSerializer, SupplierSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from users.serializer import * 
from users.models import User


class BuyerRegistrationView(RegisterView):
    serializer_class = BuyerCustomRegistrationSerializer
# Create your views here.
class FarmerData(APIView):
    # allow access to only authenticated users
    # this requires a jwt token
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, format = None):
        farmer_data = Farmer.objects.all()
        serializers = FarmerSerializer(farmer_data, many=True)
        return Response(serializers.data)
    def post(self, request, format = None):
        serializers = FarmerSerializer(data = request.data)
        if serializers.is_valid():
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
                'user': serializer.data
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

class UserListView(APIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        if user.role == 1 or user.role == 2 or user.role == 3 or user.role == 4:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return response(response, status.HTTP_403_FORBIDDEN)
        else:
            users = User.objects.all()
            serializer = self.serializer_class(users, many=True)
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Successfully fetched users',
                'users': serializer.data


            }
        return Response(response, status=status.HTTP_200_OK)

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

