from django.conf.urls import handler400, handler403, handler404, handler500
from django.urls import path, include

from django.contrib.auth import views as auth_views
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('', include('api.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    handler400 = 'api.views.bad_request'
    handler403 = 'api.views.permission_denied'
    handler404 = 'api.views.page_not_found'
    handler500 = 'api.views.server_error'