from uuid import UUID

from domain.air_quality_metrics.air_quality_metric import AirQualityMetric
from .air_quality_metric import AirQualityMetricModel


class DjangoAirQualityMetricRepository:
    def get_by_id(self, air_quality_metric_id: UUID) -> AirQualityMetric | None:
        obj = AirQualityMetricModel.objects.get(id=air_quality_metric_id)
        if not obj:
            return None
        return obj.to_domain()
