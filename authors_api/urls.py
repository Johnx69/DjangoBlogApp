from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Authors Haven API",
        default_version="v1",
        description="Authors Haven API Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hoanganh692004@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
    ),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Authors Haven Admin"
admin.site.site_title = "Authors Haven Admin Portal"
admin.site.index_title = "Welcome to Authors Haven Portal"
