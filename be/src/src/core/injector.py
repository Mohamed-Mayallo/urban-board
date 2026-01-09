from injector import Injector, Module, provider, singleton

from app.population_records.growth_over_time_usecase import GrowthOverTimeUseCase
from app.users.me_usecase import MeUseCase
from domain.population_records.population_record_repository import PopulationRecordRepository
from domain.users.user_repository import UserRepository
from persist.population_records.population_record_repository_django import DjangoPopulationRecordRepository
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

    @singleton
    @provider
    def provide_population_record_repository(self) -> PopulationRecordRepository:
        return DjangoPopulationRecordRepository()

    @singleton
    @provider
    def provide_population_records_growth_over_time_usecase(
        self, repo: PopulationRecordRepository
    ) -> GrowthOverTimeUseCase:
        return GrowthOverTimeUseCase(repo)


injector = Injector([AppModule()])
