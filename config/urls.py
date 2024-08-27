from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.settings import MEDIA_ROOT, MEDIA_URL
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('user/', include('authen_drf.urls', namespace='user')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('', include('lms.urls', namespace='lms'))
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
