
from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.models import User
# from rest_framework import generics, permissions, mixins
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.authentication import get_authorization_header
# from rest_framework.permissions import IsAuthenticated 
# from .serializer import RegisterSerializer, UserSerializer
from rest_auth.registration.views import RegisterView
from .serializer import (
    SupplierCustomRegistrationSerializer, BuyerCustomRegistrationSerializer
    )

class SupplierRegistrationView(RegisterView):
    serializer_class = SupplierCustomRegistrationSerializer


class BuyerRegistrationView(RegisterView):
    serializer_class = BuyerCustomRegistrationSerializer
# Create your views here.

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