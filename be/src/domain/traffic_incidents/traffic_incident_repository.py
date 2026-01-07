from typing import Protocol
from uuid import UUID

from .traffic_incident import TrafficIncident


class TrafficIncidentRepository(Protocol):
    def get_by_id(self, traffic_incident_id: UUID) -> TrafficIncident | None:
        ...
