from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class City:
    id: UUID
    name: str
    country: str
    latitude: int
    longitude: int
