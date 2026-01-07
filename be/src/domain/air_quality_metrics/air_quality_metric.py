from dataclasses import dataclass
from uuid import UUID

from domain.cities.city import City


@dataclass(frozen=True)
class AirQualityMetric:
    id: UUID
    recorded_at: str
    pm25: float
    pm10: float
    no2: float
    o3: float
    city_id: UUID | None = None
    city: City | None = None
