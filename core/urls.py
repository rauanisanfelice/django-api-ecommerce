from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('api/', include('api.urls')),
]