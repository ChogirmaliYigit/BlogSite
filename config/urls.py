from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as drf_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = drf_schema_view(
    openapi.Info(
    title="Cho'girmali Blog API",
    description="Cho'girmali Blog saytining api'dan foydalanish bo'yicha dokumentatsiya",
    default_version='v1',
    terms_of_service='https://www.google.com/policies/terms/',
    contact=openapi.Contact(email='chogirmali.yigit@gmal.com')
    ),
    public=True,
    permission_classes=(AllowAny, )
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('auth/', include('auth.urls')),
    path('main/', include('main.urls')),
    path('api/v1/', include('api.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('schema/', get_schema_view(title="Cho'girmali Blog API", description="Cho'girmali Blog saytining api'dan foydalanish bo'yicha dokumentatsiya", version='1.0.0'), name='openapi-schema'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),
]

if settings.DEBUG:
    urlpatterns += static(
        prefix=settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

