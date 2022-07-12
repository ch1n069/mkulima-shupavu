from django.urls import path,include
# from .views import RegisterApi
from . import views
from django.contrib.auth import views as auth_view
# from .views import SupplierRegistrationView, BuyerRegistrationView

urlpatterns = [
    # path('', views.home , name='home'),
 
    #  #Registration Urls
    # path('registration/supplier/', SupplierRegistrationView.as_view(), name='register-supplier'),
    # path('registration/buyer/', BuyerRegistrationView.as_view(), name='register-buyer'),
    # path('login/',UserLoginView.as_view(), name='login'),
    
]

 
