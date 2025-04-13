from rest_framework.permissions import BasePermission

class UserIsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method:
            return request.user and request.user.is_authenticated and request.user.is_admin