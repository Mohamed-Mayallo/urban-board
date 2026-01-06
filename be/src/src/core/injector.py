from injector import Injector, Module, provider, singleton

from app.users.me_usecase import MeUseCase
from domain.users.user_repository import UserRepository
from persist.users.user_repository_django import DjangoUserRepository


class AppModule(Module):
    @singleton
    @provider
    def provide_task_repository(self) -> UserRepository:
        return DjangoUserRepository()

    @singleton
    @provider
    def provide_me_usecase(self) -> MeUseCase:
        return MeUseCase()


injector = Injector([AppModule()])
