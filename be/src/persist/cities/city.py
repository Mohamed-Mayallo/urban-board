import uuid
from django.db import models
from domain.cities.city import City


class CityModel(models.Model):
    id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4
    )  # type: ignore[assignment]
    name: str = models.CharField(max_length=255)  # type: ignore[assignment]
    country: str = models.CharField(max_length=100)  # type: ignore[assignment]
    latitude: int = models.FloatField()  # type: ignore[assignment]
    longitude: int = models.FloatField()  # type: ignore[assignment]

    class Meta:
        db_table = "cities"
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["id"]

    def __str__(self):
        return self.name

    def to_domain(self) -> City:
        return City(
            id=self.id,
            name=self.name,
            country=self.country,
            latitude=self.latitude,
            longitude=self.longitude,
        )
