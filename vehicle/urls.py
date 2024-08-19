from os.path import basename

from django.urls import path
from rest_framework.routers import DefaultRouter

from vehicle.apps import VehicleConfig
from vehicle.views import VehicleViewSet, BikeCreateAPIView, BikeListAPIView

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'vehicle', VehicleViewSet, basename='vehicle')

urlpatterns = [
    path('bike/create/', BikeCreateAPIView.as_view(), name='bike_create'),
    path('bike/', BikeListAPIView.as_view(), name='bike_list')
] + router.urls


