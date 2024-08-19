from rest_framework.routers import DefaultRouter

from vehicle.apps import VehicleConfig
from vehicle.views import VehicleViewSet

app_name = VehicleConfig.name

router = DefaultRouter()
router.register('vehicle', VehicleViewSet, basename='vehicle')

urlpatterns = [] + router.urls


