from rest_framework import permissions


class IsAdmin_CriticOrReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        return (
            request.user.is_superuser
            or request.method in permissions.SAFE_METHODS
            or request.user.is_critic
        )
