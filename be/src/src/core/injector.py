from injector import Injector, Module, provider, singleton

from app.population_records.growth_over_time_usecase import GrowthOverTimeUseCase
from app.traffic_incidents.incidents_over_time_usecase import IncidentsOverTimeUseCase
from app.users.me_usecase import MeUseCase
from domain.population_records.population_record_repository import PopulationRecordRepository
from domain.traffic_incidents.traffic_incident_repository import TrafficIncidentRepository
from domain.users.user_repository import UserRepository
from persist.population_records.population_record_repository_django import DjangoPopulationRecordRepository
from persist.traffic_incidents.traffic_incident_repository_django import DjangoTrafficIncidentRepository
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

    @singleton
    @provider
    def provide_traffic_incident_repository(self) -> TrafficIncidentRepository:
        return DjangoTrafficIncidentRepository()

    @singleton
    @provider
    def provide_incidents_over_time_usecase(self, repo: TrafficIncidentRepository) -> IncidentsOverTimeUseCase:
        return IncidentsOverTimeUseCase(repo)


injector = Injector([AppModule()])
