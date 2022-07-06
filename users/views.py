
from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.models import User
# from rest_framework import generics, permissions, mixins
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.authentication import get_authorization_header
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .serializer import RegisterSerializer, UserSerializer
from rest_auth.registration.views import RegisterView
from .serializer import (
    SupplierCustomRegistrationSerializer, BuyerCustomRegistrationSerializer
    )

class SupplierRegistrationView(RegisterView):
    permission_class = (IsAuthenticatedOrReadOnly)
    serializer_class = SupplierCustomRegistrationSerializer


class BuyerRegistrationView(RegisterView):
    permission_class = (IsAuthenticatedOrReadOnly)
    serializer_class = BuyerCustomRegistrationSerializer
# Create your views here.

def home(request):
    return render(request, 'home.html')

