from typing import Protocol
from uuid import UUID

from .user import User


class UserRepository(Protocol):
    def getById(self, user_id: UUID) -> User | None:
        ...
