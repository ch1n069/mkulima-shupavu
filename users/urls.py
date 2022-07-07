
from django.urls import path, re_path
# from .views import RegisterApi
from . import views 
from django.conf import settings
from django.conf.urls.static import static

from users.views import *
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('', views.home , name='home'),
    # path('api/register', RegisterApi.as_view()),
     #Registration Urls
    path('registration/supplier/', SupplierRegistrationView.as_view(), name='register-seller'),
    path('registration/buyer/', BuyerRegistrationView.as_view(), name='register-buyer'),
    re_path(r'^api/farmer/$', views.FarmerData.as_view()),

    # re_path(r'^api/buyer/$', views.BuyerData.as_view()),
    # re_path(r'^api/supplier/$', views.SupplierData.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name = 'token_refresh'),
    path('register', AuthUserRegistrationView.as_view(), name='register'),
    path('login', AuthUserLoginView.as_view(), name='login'),
    path('users', UserListView.as_view(), name='users')
]


    
] if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

