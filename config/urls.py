from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='UVA API',
        terms_of_services="",
        default_version='v1',
        # contact=openapi.Contact(email="a@gmail.com"),
        # license=openapi.License(name="License"),

    ),

    public=False,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui", ),
    path('admin/', admin.site.urls),
    path('', include('locomotiv.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
