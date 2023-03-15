from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('auth/', include('auth.urls')),
    path('main/', include('main.urls')),
    path('api/v1/', include('api.urls')),
    path('api/auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        prefix=settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

