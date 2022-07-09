from django.urls import path, re_path
from users import views
from django.conf import settings
from django.conf.urls.static import static
from users.views import *
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
# router for the userlistview which is a viewset. the methods are list and retrieve
router.register(r'api/users', views.UserListView, basename='users list')

urlpatterns = [
    re_path(r'^api/farmer/$', views.FarmerData.as_view()),
    re_path(r'^api/buyer/$', views.BuyerData.as_view()),
    re_path(r'^api/supplier/$', views.SupplierData.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name = 'token_refresh'),
    path('register', AuthUserRegistrationView.as_view(), name='register'),
    path('login', AuthUserLoginView.as_view(), name='login'),
    
    # path('users', UserListView.as_view({'get': 'list'}), name='users')
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)