
from django.urls import path, re_path
# from .views import RegisterApi
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .views import SupplierRegistrationView, BuyerRegistrationView



urlpatterns = [
    path('', views.home , name='home'),
    # path('api/register', RegisterApi.as_view()),
     #Registration Urls
    path('registration/supplier/', SupplierRegistrationView.as_view(), name='register-seller'),
    path('registration/buyer/', BuyerRegistrationView.as_view(), name='register-buyer'),
    re_path(r'^api/farmer/$', views.FarmerData.as_view()),
    re_path(r'^api/buyer/$', views.BuyerData.as_view()),
    re_path(r'^api/supplier/$', views.SupplierData.as_view()),

    
] 

if settings.DEBUG: 
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

