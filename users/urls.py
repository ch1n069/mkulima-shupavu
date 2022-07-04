from django.urls import path, re_path
from users import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    re_path(r'^api/farmer/$', views.FarmerData.as_view()),
    re_path(r'^api/buyer/$', views.BuyerData.as_view()),
    re_path(r'^api/supplier/$', views.SupplierData.as_view()),
    re_path(r'^api/agent/$', views.AgentData.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)