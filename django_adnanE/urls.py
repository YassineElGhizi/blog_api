from django.contrib import admin
from django.urls import path, include, re_path

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title="Blogs API", default_version='v1', description="API documentation", ), public=False,
    permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blogs.urls')),

    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
