from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authen_drf.urls')),
    path('', include('lms.urls', namespace='lms'))
]
