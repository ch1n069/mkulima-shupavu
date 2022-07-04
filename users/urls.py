from django.urls import path,include
# from .views import RegisterApi
from . import views
from django.contrib.auth import views as auth_view
from .views import SupplierRegistrationView, BuyerRegistrationView

urlpatterns = [
    path('', views.home , name='home'),
    # path('api/register', RegisterApi.as_view()),
     #Registration Urls
    path('registration/supplier/', SupplierRegistrationView.as_view(), name='register-seller'),
    path('registration/buyer/', BuyerRegistrationView.as_view(), name='register-buyer'),
    
]

 
