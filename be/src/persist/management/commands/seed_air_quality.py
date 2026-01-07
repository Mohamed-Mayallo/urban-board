import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from persist.cities.city import CityModel
from ...air_quality_metrics.air_quality_metric import AirQualityMetricModel


class Command(BaseCommand):
    help = "Seed air quality metrics for all cities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--days",
            type=int,
            default=30,
            help="Number of days to seed",
        )

        parser.add_argument(
            "--interval",
            type=int,
            default=15,
            help="Interval in minutes between records",
        )

        parser.add_argument(
            "--truncate",
            action="store_true",
            help="Delete existing records before seeding",
        )

    def handle(self, *_, **options):
        days = options["days"]
        interval = options["interval"]

        end_time = now()
        start_time = end_time - timedelta(days=days)

        if options["truncate"]:
            AirQualityMetricModel.objects.all().delete()
            self.stdout.write("Existing records deleted")

        self.stdout.write(
            f"Seeding air quality data from {start_time} to {end_time}"
        )

        records = []

        for city in CityModel.objects.all():
            current_time = start_time

            # baseline values per city (simulates real differences)
            base_pm25 = random.uniform(10, 30)
            base_pm10 = random.uniform(20, 50)
            base_no2 = random.uniform(15, 40)
            base_o3 = random.uniform(20, 60)

            while current_time <= end_time:
                records.append(
                    AirQualityMetricModel(
                        city=city,
                        recorded_at=current_time,
                        pm25=max(0, base_pm25 + random.uniform(-5, 5)),
                        pm10=max(0, base_pm10 + random.uniform(-10, 10)),
                        no2=max(0, base_no2 + random.uniform(-8, 8)),
                        o3=max(0, base_o3 + random.uniform(-10, 10)),
                    )
                )

                current_time += timedelta(minutes=interval)

        AirQualityMetricModel.objects.bulk_create(records, batch_size=5000)

        self.stdout.write(
            self.style.SUCCESS(
                f"Inserted {len(records)} air quality records"
            )
        )
