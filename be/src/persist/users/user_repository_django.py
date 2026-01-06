from uuid import UUID

from domain.users.user import User
from .user import UserModel


class DjangoUserRepository:
    def getById(self, user_id: UUID) -> User | None:
        obj = UserModel.objects.get(id=user_id)
        if not obj:
            return None
        return User(**obj.to_domain_user())
