from domain.users.user import User


class MeUseCase:
    def execute(self, user: User) -> User:
        return user
