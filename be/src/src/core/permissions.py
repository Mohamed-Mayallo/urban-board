from rest_framework.permissions import BasePermission
from domain.users.user import Roles


class HasRole(BasePermission):
    allowed_roles: list[Roles] = []

    def has_permission(self, request):
        return (
            request.user.is_authenticated
            and request.user.role in self.allowed_roles
        )
