from uuid import UUID

from domain.traffic_incidents.traffic_incident import TrafficIncident
from .traffic_incident import TrafficIncidentModel


class DjangoTrafficIncidentRepository:
    def get_by_id(self, traffic_incident_id: UUID) -> TrafficIncident | None:
        obj = TrafficIncidentModel.objects.get(id=traffic_incident_id)
        if not obj:
            return None
        return obj.to_domain()
