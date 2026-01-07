import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from persist.traffic_incidents.traffic_incident import TrafficIncidentModel
from persist.cities.city import CityModel


class Command(BaseCommand):
    help = "Seed traffic incidents for all cities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--per-city",
            type=int,
            default=1000,
            help="Number of incidents to generate per city",
        )

        parser.add_argument(
            "--days",
            type=int,
            default=7,
            help="Number of past days to spread incidents across",
        )

        parser.add_argument(
            "--truncate",
            action="store_true",
            help="Delete existing records before seeding",
        )

    def handle(self, *_, **options):
        per_city = options["per_city"]
        days = options["days"]

        if options["truncate"]:
            TrafficIncidentModel.objects.all().delete()
            self.stdout.write("Existing records deleted")

        self.stdout.write(
            f"Seeding traffic incidents ({per_city} per city, last {days} days)"
        )

        incident_types = ["accident", "roadblock", "construction"]

        end_time = now()
        start_time = end_time - timedelta(days=days)

        records = []

        for city in CityModel.objects.all():
            for _ in range(per_city):
                occurred_at = start_time + timedelta(
                    seconds=random.randint(
                        0, int((end_time - start_time).total_seconds())
                    )
                )

                records.append(
                    TrafficIncidentModel(
                        city=city,
                        incident_type=random.choice(incident_types),
                        severity=random.randint(1, 5),
                        occurred_at=occurred_at,

                        # small geo jitter around city center
                        latitude=city.latitude + random.uniform(-0.1, 0.1),
                        longitude=city.longitude + random.uniform(-0.1, 0.1),
                    )
                )

        TrafficIncidentModel.objects.bulk_create(
            records,
            batch_size=5000,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Inserted {len(records)} traffic incident records"
            )
        )
