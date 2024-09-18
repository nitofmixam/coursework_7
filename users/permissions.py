from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user or request.user.is_superuser:
            return True

        return False