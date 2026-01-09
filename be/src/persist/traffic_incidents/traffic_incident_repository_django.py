from datetime import date
from typing import Optional, cast
from uuid import UUID

from django.db.models import CharField, Count
from django.db.models.expressions import Case, Value, When

from domain.traffic_incidents.traffic_incident import TrafficIncident
from domain.traffic_incidents.traffic_incident_repository import IncidentsOverTimeOutput

from .traffic_incident import TrafficIncidentModel


class DjangoTrafficIncidentRepository:
    def get_by_id(self, traffic_incident_id: UUID) -> TrafficIncident | None:
        obj = TrafficIncidentModel.objects.get(id=traffic_incident_id)
        if not obj:
            return None
        return obj.to_domain()

    def incidents_over_time(
        self, city_id: UUID, start_date: Optional[date], end_date: Optional[date]
    ) -> list[IncidentsOverTimeOutput]:
        qs = TrafficIncidentModel.objects.filter(city_id=city_id)

        if start_date:
            qs = qs.filter(occurred_at__gte=start_date)

        if end_date:
            qs = qs.filter(occurred_at__lte=end_date)

        res_qs = (
            qs.annotate(
                severity_label=(
                    Case(
                        When(severity__in=[1, 2], then=Value("Low")),
                        When(severity__in=[3], then=Value("Medium")),
                        When(severity__in=[4, 5], then=Value("High")),
                        default=Value("Unknown"),
                        output_field=CharField(),
                    )
                )
            )
            .values("severity_label")
            .annotate(count=Count("id"))
        )

        return cast(list[IncidentsOverTimeOutput], list(res_qs))
