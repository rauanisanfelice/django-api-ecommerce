from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

from api.views import UserList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('openapi-schema/', get_schema_view(
        title="E-Commerce", 
        description="Django API E-Commerce",
        version="1.0.0",
        public=True,
    ), name='openapi-schema'), 

    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]