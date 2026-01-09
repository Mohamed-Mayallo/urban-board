from datetime import date
from typing import Literal, Optional, cast
from uuid import UUID

from django.db.models import CharField, Sum, Value
from django.db.models.expressions import Func

from domain.population_records.population_record import PopulationRecord
from domain.population_records.population_record_repository import GetGrowthOverTimeOutput

from .population_record import PopulationRecordModel


class DjangoPopulationRecordRepository:
    def get_by_id(self, population_record_id: UUID) -> PopulationRecord | None:
        obj = PopulationRecordModel.objects.get(id=population_record_id)
        if not obj:
            return None
        return obj.to_domain()

    def get_growth_over_time(
        self,
        city_id: UUID,
        start_date: Optional[date],
        end_date: Optional[date],
        granularity: Optional[Literal["year", "month"]],
    ) -> list[GetGrowthOverTimeOutput]:
        qs = PopulationRecordModel.objects.filter(city_id=city_id)

        if start_date:
            qs = qs.filter(date__gte=start_date)

        if end_date:
            qs = qs.filter(date__lte=end_date)

        if granularity is None:
            granularity = "year"

        date_format = "YYYY" if granularity == "year" else "YYYY-MM"

        res_qs = (
            qs.annotate(
                period=Func(
                    "date",
                    Value(date_format),
                    function="to_char",
                    output_field=CharField(),
                    # date_format=date_format,
                    # template="%(function)s(%(expressions)s, '%(date_format)s')"
                )
            )
            .values("period")
            .annotate(population=Sum("population"))
            .order_by("period")
        )

        return cast(list[GetGrowthOverTimeOutput], list(res_qs))
