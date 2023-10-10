from rest_framework import permissions

from users.models import UserRole


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == UserRole.MODERATOR:
            return True
        return False


class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == UserRole.MEMBER:
            return True
        return False


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False

