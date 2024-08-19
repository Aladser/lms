from rest_framework import serializers

from vehicle.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    model = Vehicle
    fields = '__all__'
