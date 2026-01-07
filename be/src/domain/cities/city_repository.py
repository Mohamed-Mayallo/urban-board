from typing import Protocol
from uuid import UUID

from .city import City


class CityRepository(Protocol):
    def getById(self, city_id: UUID) -> City | None:
        ...
