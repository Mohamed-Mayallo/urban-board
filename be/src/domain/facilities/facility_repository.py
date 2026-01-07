from typing import Protocol
from uuid import UUID

from .facility import Facility


class FacilityRepository(Protocol):
    def get_by_id(self, facility_id: UUID) -> Facility | None:
        ...
