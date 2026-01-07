from dataclasses import dataclass
from uuid import UUID

from domain.cities.city import City


@dataclass(frozen=True)
class TrafficIncident:
    id: UUID
    incident_type: str
    severity: int
    occurred_at: str
    latitude: float
    longitude: float
    city_id: UUID | None = None
    city: City | None = None
