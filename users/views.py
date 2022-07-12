
from django.http import HttpResponse
from django.shortcuts import render
from users.models import *

from django.contrib.auth.models import User
from rest_framework import generics, permissions, mixins 
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework.permissions import IsAuthenticated 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from .serializer import RegisterSerializer, UserSerializer
from users.serializer import *

from rest_auth.registration.views import RegisterView
from .serializer import (
    SupplierCustomRegistrationSerializer, BuyerCustomRegistrationSerializer
    )

class SupplierRegistrationView(RegisterView):
    serializer_class = SupplierCustomRegistrationSerializer


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


def home(request):
    return render(request, 'home.html')



# #Register API
# class RegisterApi(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
#     def post(self, request, *args,  **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializer(user,    context=self.get_serializer_context()).data,
#             "message": "User Created Successfully.  Now perform Login to get your token",
#         })

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

