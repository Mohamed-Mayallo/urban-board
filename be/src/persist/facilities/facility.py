import uuid
from django.db import models
from domain.cities.city import City
from ..cities.city import CityModel
from domain.facilities.facility import Facility
from domain.facilities.facility import FacilityType


class FacilityModel(models.Model):

    id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4
    )  # type: ignore[assignment]
    city: City = models.ForeignKey(
        CityModel, on_delete=models.CASCADE)  # type: ignore[assignment]
    name: str = models.CharField(
        max_length=255)  # type: ignore[assignment]
    facility_type: FacilityType = models.CharField(
        # type: ignore[assignment]
        choices=[(choice.value, choice.name) for choice in FacilityType])
    latitude: float = models.FloatField()  # type: ignore[assignment]
    longitude: float = models.FloatField()  # type: ignore[assignment]

    class Meta:
        db_table = "facilities"
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"
        ordering = ["id"]

    def to_domain(self) -> Facility:
        return Facility(
            id=self.id,
            city_id=self.city.id,
            city=self.city,
            name=self.name,
            facility_type=self.facility_type,
            latitude=self.latitude,
            longitude=self.longitude,
        )
