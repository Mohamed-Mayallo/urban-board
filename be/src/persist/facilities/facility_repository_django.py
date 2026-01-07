from uuid import UUID

from domain.facilities.facility import Facility
from .facility import FacilityModel


class DjangoFacilityRepository:
    def get_by_id(self, facility_id: UUID) -> Facility | None:
        obj = FacilityModel.objects.get(id=facility_id)
        if not obj:
            return None
        return obj.to_domain()
