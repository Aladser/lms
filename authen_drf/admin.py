from django.contrib import admin

from authen_drf.models import User, Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
