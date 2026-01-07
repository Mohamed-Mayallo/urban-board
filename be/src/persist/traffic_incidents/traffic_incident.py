import uuid
from django.db import models
from domain.cities.city import City
from ..cities.city import CityModel
from domain.traffic_incidents.traffic_incident import TrafficIncident


class TrafficIncidentModel(models.Model):
    id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4
    )  # type: ignore[assignment]
    city: City = models.ForeignKey(
        CityModel, on_delete=models.CASCADE)  # type: ignore[assignment]
    incident_type: str = models.CharField(
        max_length=100)  # type: ignore[assignment]
    severity: int = models.IntegerField()  # type: ignore[assignment]
    occurred_at: str = models.DateTimeField()  # type: ignore[assignment]
    latitude: float = models.FloatField()  # type: ignore[assignment]
    longitude: float = models.FloatField()  # type: ignore[assignment]

    class Meta:
        db_table = "traffic_incidents"
        verbose_name = "Traffic Incident"
        verbose_name_plural = "Traffic Incidents"
        ordering = ["id"]

    def to_domain(self) -> TrafficIncident:
        return TrafficIncident(
            id=self.id,
            city_id=self.city.id,
            city=self.city,
            incident_type=self.incident_type,
            severity=self.severity,
            occurred_at=self.occurred_at,
            latitude=self.latitude,
            longitude=self.longitude,
        )
