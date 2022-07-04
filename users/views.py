from django.shortcuts import render
from users.models import Farmer, Buyer, Supplier, Agent
from users.serializer import FarmerSerializer, BuyerSerializer, SupplierSerializer, AgentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

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