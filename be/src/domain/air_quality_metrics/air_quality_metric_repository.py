from typing import Protocol
from uuid import UUID

from .air_quality_metric import AirQualityMetric


class AirQualityMetricRepository(Protocol):
    def get_by_id(self, air_quality_metric_id: UUID) -> AirQualityMetric | None:
        ...
