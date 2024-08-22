from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authen_drf.urls', namespace='user')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('', include('lms.urls', namespace='lms'))
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
