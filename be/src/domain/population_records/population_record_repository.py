from typing import Protocol
from uuid import UUID

from .population_record import PopulationRecord


class PopulationRecordRepository(Protocol):
    def getById(self, population_record_id: UUID) -> PopulationRecord | None:
        ...
