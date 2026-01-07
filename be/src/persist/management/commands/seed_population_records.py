import random
import uuid
from datetime import date, timedelta

from django.core.management.base import BaseCommand

from persist.population_records.population_record import PopulationRecordModel
from persist.cities.city import CityModel


class Command(BaseCommand):
    help = "Seed population records for all cities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--start-year",
            type=int,
            default=2015,
            help="Start year for population data",
        )

        parser.add_argument(
            "--end-year",
            type=int,
            default=2024,
            help="End year for population data",
        )

        parser.add_argument(
            "--interval-days",
            type=int,
            default=30,
            help="Days between population records",
        )

        parser.add_argument(
            "--truncate",
            action="store_true",
            help="Delete existing records before seeding",
        )

    def handle(self, *_, **options):
        start_year = options["start_year"]
        end_year = options["end_year"]
        interval_days = options["interval_days"]

        start_date = date(start_year, 1, 1)
        end_date = date(end_year, 1, 1)

        if options["truncate"]:
            PopulationRecordModel.objects.all().delete()
            self.stdout.write("Existing records deleted")

        self.stdout.write(
            f"Seeding population records from {start_date} to {end_date}"
        )

        records = []

        for city in CityModel.objects.all():
            # baseline population per city
            population = random.randint(500_000, 3_000_000)
            current_date = start_date

            while current_date <= end_date:
                # realistic population drift
                population_change = random.randint(-2_000, 5_000)
                population = max(0, population + population_change)

                records.append(
                    PopulationRecordModel(
                        id=uuid.uuid4(),
                        city_id=city.id,
                        date=current_date,
                        population=population,
                    )
                )

                current_date += timedelta(days=interval_days)

        PopulationRecordModel.objects.bulk_create(
            records,
            ignore_conflicts=True,
            batch_size=5000,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Inserted {len(records)} population records"
            )
        )
