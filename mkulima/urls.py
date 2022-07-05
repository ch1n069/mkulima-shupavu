"""mkulima URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views


admin.site.site_header = 'Super Mkulima Admin'
admin.site.site_title = 'Super Mkulima Admin'
admin.site.index_title = 'Super Mkulima Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name = 'token_refresh'),
]

# api/token/ provides access for a 5 minute period token before expiry
# api/token/refresh/ provides access for a 24 hour period token before expiry

