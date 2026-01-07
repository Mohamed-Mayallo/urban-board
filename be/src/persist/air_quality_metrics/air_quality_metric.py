import uuid
from django.db import models
from domain.cities.city import City
from ..cities.city import CityModel
from domain.air_quality_metrics.air_quality_metric import AirQualityMetric


class AirQualityMetricModel(models.Model):
    id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4
    )  # type: ignore[assignment]
    city: City = models.ForeignKey(
        CityModel, on_delete=models.CASCADE)  # type: ignore[assignment]
    recorded_at: str = models.DateTimeField()  # type: ignore[assignment]
    pm25: float = models.FloatField()  # type: ignore[assignment]
    pm10: float = models.FloatField()  # type: ignore[assignment]
    no2: float = models.FloatField()  # type: ignore[assignment]
    o3: float = models.FloatField()  # type: ignore[assignment]

    class Meta:
        db_table = "air_quality_metrics"
        verbose_name = "Air Quality Metric"
        verbose_name_plural = "Air Quality Metrics"
        ordering = ["id"]
        indexes = [
            models.Index(fields=["city", "recorded_at"]),
        ]

    def to_domain(self) -> AirQualityMetric:
        return AirQualityMetric(
            id=self.id,
            city_id=self.city.id,
            city=self.city,
            recorded_at=self.recorded_at,
            pm25=self.pm25,
            pm10=self.pm10,
            no2=self.no2,
            o3=self.o3,
        )
