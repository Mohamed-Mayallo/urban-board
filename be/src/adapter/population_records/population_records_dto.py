from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel, PastDate


class GrowthOverTimeOutputDTO(BaseModel):
    period: str
    population: int


class GrowthOverTimeInputDto(BaseModel):
    city_id: UUID
    start_date: Optional[PastDate]
    end_date: Optional[PastDate]
    granularity: Optional[Literal["year", "month"]]
