from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    """Проверка прав на владельца"""
    message = "Вы не владелец!"

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsOwner(BasePermission):
    """Проверка на создателя привычки"""
    message = "Вы не создатель!"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
