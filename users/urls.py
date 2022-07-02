from django.urls import path
from .views import RegisterApi


urlpatterns = [
    # path('', home , name='home'),
    path('api/register', RegisterApi.as_view()),
 
]