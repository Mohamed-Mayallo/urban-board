from uuid import UUID

from domain.cities.city import City
from .city import CityModel


class DjangoCityRepository:
    def getById(self, city_id: UUID) -> City | None:
        obj = CityModel.objects.get(id=city_id)
        if not obj:
            return None
        return obj.to_domain()
