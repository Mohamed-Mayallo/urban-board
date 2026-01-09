from typing import Optional
from uuid import UUID

from pydantic import BaseModel, FutureDate, PastDate


class IncidentsOverTimeOutputDTO(BaseModel):
    severity_label: str
    count: int


class IncidentsOverTimeInputDto(BaseModel):
    city_id: UUID
    start_date: Optional[PastDate]
    end_date: Optional[FutureDate]
