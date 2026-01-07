from dataclasses import dataclass
from uuid import UUID

from domain.cities.city import City

from enum import StrEnum


class FacilityType(StrEnum):
    HOSPITAL = "hospital"
    SCHOOL = "school"
    POLICE = "police"
    FIRE_STATION = "fire_station"
    PARK = "park"
    LIBRARY = "library"
    METRO_STATION = "metro_station"


@dataclass(frozen=True)
class Facility:
    id: UUID
    name: str
    facility_type: FacilityType
    latitude: float
    longitude: float
    city_id: UUID | None = None
    city: City | None = None
