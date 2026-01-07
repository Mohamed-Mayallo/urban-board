import random
from django.core.management.base import BaseCommand
from persist.cities.city import CityModel
from persist.facilities.facility import FacilityModel
from domain.facilities.facility import FacilityType


class Command(BaseCommand):
    help = "Seed facilities for all cities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--min",
            type=int,
            default=50,
            help="Minimum facilities per city",
        )

        parser.add_argument(
            "--max",
            type=int,
            default=300,
            help="Maximum facilities per city",
        )

        parser.add_argument(
            "--truncate",
            action="store_true",
            help="Delete existing facilities before seeding",
        )

    def handle(self, *_, **options):
        min_count = options["min"]
        max_count = options["max"]

        if options["truncate"]:
            FacilityModel.objects.all().delete()
            self.stdout.write("Existing facilities deleted")

        records = []

        for city in CityModel.objects.all():
            count = random.randint(min_count, max_count)

            for i in range(count):
                facility_type = random.choice(
                    [choice for choice in FacilityType]
                )

                records.append(
                    FacilityModel(
                        city=city,
                        name=f"{city.name} {facility_type.replace('_', ' ').title()} {i + 1}",
                        facility_type=facility_type,
                        latitude=city.latitude + random.uniform(-0.05, 0.05),
                        longitude=city.longitude + random.uniform(-0.05, 0.05),
                    )
                )

        FacilityModel.objects.bulk_create(records, batch_size=1000)

        self.stdout.write(
            self.style.SUCCESS(
                f"Inserted {len(records)} facility records"
            )
        )
