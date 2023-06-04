from rest_framework import permissions


class IsOwnerOrIsAdmin(permissions.BasePermission):
    message = "Please register to access this page."

    def has_object_permission(self, request, view, obj):
        return bool(obj.id == request.user.id or request.user.is_staff)


class IsOwner(permissions.IsAuthenticated):
    message = "For have permission to perform this action you should be owner."

    def has_permission(self, request, view):
        return (
            super().has_permission(request=request, view=view) and request.user.is_owner
        )
