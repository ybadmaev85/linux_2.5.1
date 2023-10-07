from rest_framework import permissions

from users.models import UserRole


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRole.MODERATOR and request.method in ('GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH')