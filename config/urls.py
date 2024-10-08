from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from config.settings import MEDIA_ROOT, MEDIA_URL

schema_view = get_schema_view(
   openapi.Info(
      title="LMS API",
      default_version='v1',
      description="Платформа для онлайн-обучения",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authen_drf.urls', namespace='user')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('lms.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
