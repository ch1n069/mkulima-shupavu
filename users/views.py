
from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.models import User
# from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
# from rest_framework.views import APIView
# from rest_framework.authentication import get_authorization_header
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .serializer import RegisterSerializer, UserSerializer
from rest_auth.registration.views import RegisterView
# from .serializer import (
#     SupplierCustomRegistrationSerializer, BuyerCustomRegistrationSerializer, UserLoginSerializer
#     )

# class SupplierRegistrationView(RegisterView):
#     permission_class = (IsAuthenticatedOrReadOnly)
#     serializer_class = SupplierCustomRegistrationSerializer


# class BuyerRegistrationView(RegisterView):
#     permission_class = (IsAuthenticatedOrReadOnly)
#     serializer_class = BuyerCustomRegistrationSerializer



# # login view
# class UserLoginView(RetrieveAPIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     serializer_class = UserLoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         response = {
#             'success' : 'True',
#             'status code' : status.HTTP_200_OK,
#             'message': 'User logged in  successfully',
#             'token' : serializer.data['token'],
#             }
#         status_code = status.HTTP_200_OK

#         return Response(response, status=status_code)
    

# def home(request):
#     return render(request, 'home.html')

