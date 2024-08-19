from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from vehicle.models import Vehicle, Bike
from vehicle.serializares import VehicleSerializer, BikeSerializer


class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

class BikeListAPIView(generics.ListAPIView):
    serializer_class = BikeSerializer
    queryset = Bike.objects.all()

class BikeCreateAPIView(generics.CreateAPIView):
    serializer_class = BikeSerializer


