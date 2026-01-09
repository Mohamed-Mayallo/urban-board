from datetime import date
from typing import Literal, Optional, Protocol, TypedDict
from uuid import UUID

from .population_record import PopulationRecord


class GetGrowthOverTimeOutput(TypedDict):
    period: str
    population: int


class PopulationRecordRepository(Protocol):
    def get_by_id(self, population_record_id: UUID) -> PopulationRecord | None:
        ...

    def get_growth_over_time(
        self,
        city_id: UUID,
        start_date: Optional[date],
        end_date: Optional[date],
        granularity: Optional[Literal["year", "month"]],
    ) -> list[GetGrowthOverTimeOutput]:
        ...
