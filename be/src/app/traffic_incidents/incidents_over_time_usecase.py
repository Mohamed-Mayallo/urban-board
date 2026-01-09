from datetime import date
from typing import Optional, Protocol, TypedDict
from uuid import UUID

from injector import inject

from domain.traffic_incidents.traffic_incident_repository import TrafficIncidentRepository


class IncidentsOverTimeUseCase:
    @inject
    def __init__(self, repo: TrafficIncidentRepository):
        self._repo = repo

    class _Output(TypedDict):
        severity_label: str
        count: int

    class _Input(Protocol):
        city_id: UUID
        start_date: Optional[date]
        end_date: Optional[date]

    def execute(self, input: _Input) -> list[_Output]:
        return self._repo.incidents_over_time(
            city_id=input.city_id,
            start_date=input.start_date,
            end_date=input.end_date,
        )
