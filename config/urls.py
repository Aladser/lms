from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicle/', include('vehicle.urls', namespace='vehicle'))
]
