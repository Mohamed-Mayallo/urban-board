from datetime import date
from typing import Optional, Protocol, TypedDict
from uuid import UUID

from .traffic_incident import TrafficIncident


class IncidentsOverTimeOutput(TypedDict):
    severity_label: str
    count: int


class TrafficIncidentRepository(Protocol):
    def get_by_id(self, traffic_incident_id: UUID) -> TrafficIncident | None:
        ...

    def incidents_over_time(
        self, city_id: UUID, start_date: Optional[date], end_date: Optional[date]
    ) -> list[IncidentsOverTimeOutput]:
        ...
