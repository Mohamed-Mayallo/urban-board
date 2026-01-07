import uuid
from django.db import models
from domain.cities.city import City
from ..cities.city import CityModel
from domain.population_records.population_record import PopulationRecord

from datetime import date


class PopulationRecordModel(models.Model):
    id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4
    )  # type: ignore[assignment]
    city: City = models.ForeignKey(
        CityModel, on_delete=models.CASCADE)  # type: ignore[assignment]
    date: date = models.DateField()  # type: ignore[assignment]
    population: int = models.IntegerField()  # type: ignore[assignment]

    class Meta:
        indexes = [
            models.Index(fields=["city", "date"]),
        ]
        db_table = "population_records"
        verbose_name = "Population Record"
        verbose_name_plural = "Population Records"
        ordering = ["id"]

    def __str__(self):
        return self.name

    def to_domain(self) -> PopulationRecord:
        return PopulationRecord(
            id=self.id,
            date=self.date,
            population=self.population,
            city_id=self.city.id,
            city=self.city,
        )
