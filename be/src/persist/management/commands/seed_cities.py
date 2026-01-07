import uuid

from django.core.management.base import BaseCommand

from persist.cities.city import CityModel


class Command(BaseCommand):
    help = "Seed initial cities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--truncate",
            action="store_true",
            help="Delete existing cities before seeding",
        )

    def handle(self, *_, **options):
        if options["truncate"]:
            CityModel.objects.all().delete()
            self.stdout.write("Existing cities deleted")

        self.stdout.write("Seeding cities...")

        cities = [
            {
                "name": "Berlin",
                "country": "DE",
                "latitude": 52.52,
                "longitude": 13.405,
            },
            {
                "name": "Paris",
                "country": "FR",
                "latitude": 48.8566,
                "longitude": 2.3522,
            },
            {
                "name": "London",
                "country": "UK",
                "latitude": 51.5074,
                "longitude": 0.1278,
            },
            {
                "name": "New York",
                "country": "US",
                "latitude": 40.7128,
                "longitude": -74.0060,
            },
            {
                "name": "Tokyo",
                "country": "JP",
                "latitude": 35.6895,
                "longitude": 139.6917,
            },
            {
                "name": "Sydney",
                "country": "AU",
                "latitude": -33.8688,
                "longitude": 151.2093,
            },
            {
                "name": "Rio de Janeiro",
                "country": "BR",
                "latitude": -22.9068,
                "longitude": -43.1729,
            },
            {
                "name": "Cairo",
                "country": "EG",
                "latitude": 30.0444,
                "longitude": 31.2357,
            },
            {
                "name": "Mumbai",
                "country": "IN",
                "latitude": 19.0760,
                "longitude": 72.8777,
            },
            {
                "name": "Moscow",
                "country": "RU",
                "latitude": 55.7558,
                "longitude": 37.6173,
            },
        ]

        records = [
            CityModel(
                id=uuid.uuid4(),
                name=city["name"],
                country=city["country"],
                latitude=city["latitude"],
                longitude=city["longitude"],
            )
            for city in cities
        ]

        CityModel.objects.bulk_create(
            records,
            ignore_conflicts=True,
            batch_size=100,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Inserted {len(records)} city records"
            )
        )
