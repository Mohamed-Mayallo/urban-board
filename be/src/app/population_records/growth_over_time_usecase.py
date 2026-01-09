from datetime import date
from typing import Literal, Optional, Protocol, TypedDict
from uuid import UUID

from injector import inject

from domain.population_records.population_record_repository import PopulationRecordRepository


class GrowthOverTimeUseCase:
    @inject
    def __init__(self, repo: PopulationRecordRepository):
        self._repo = repo

    class _Output(TypedDict):
        period: str
        population: int

    class _Input(Protocol):
        city_id: UUID
        start_date: Optional[date]
        end_date: Optional[date]
        granularity: Optional[Literal["year", "month"]]

    def execute(self, input: _Input) -> list[_Output]:
        return self._repo.get_growth_over_time(
            city_id=input.city_id,
            start_date=input.start_date,
            end_date=input.end_date,
            granularity=input.granularity,
        )
