from uuid import UUID

from domain.population_records.population_record import PopulationRecord
from .population_record import PopulationRecordModel


class DjangoPopulationRecordRepository:
    def get_by_id(self, population_record_id: UUID) -> PopulationRecord | None:
        obj = PopulationRecordModel.objects.get(id=population_record_id)
        if not obj:
            return None
        return obj.to_domain()
