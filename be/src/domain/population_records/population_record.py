from dataclasses import dataclass
from uuid import UUID
from datetime import date

from domain.cities.city import City


@dataclass(frozen=True)
class PopulationRecord:
    id: UUID
    date: date
    population: int
    city_id: UUID | None = None
    city: City | None = None
