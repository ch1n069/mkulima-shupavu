from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.ProfileGenericAPIView.as_view() ,name='profile'),    
]