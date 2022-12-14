from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        return request.user.is_superuser or request.method in permissions.SAFE_METHODS
