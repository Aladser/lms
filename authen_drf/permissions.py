from rest_framework import permissions

from config.settings import MODERATORS_GROUP_NAME

# проверка модератора
class IsModeratorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name=MODERATORS_GROUP_NAME).exists()

# проверка создателя объекта
class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

# проверка редактирования своего пользовательского профиля
class IsPersonalProfilePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email
