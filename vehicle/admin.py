from django.contrib import admin

from vehicle.models import Vehicle, Bike


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    pass
