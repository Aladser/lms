from rest_framework.viewsets import ModelViewSet

from vehicle.models import Vehicle
from vehicle.serializares import VehicleSerializer


class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
