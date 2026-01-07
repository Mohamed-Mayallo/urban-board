from dataclasses import dataclass
from uuid import UUID

from enum import Enum
from domain.cities.city import City


class Roles(Enum):
    SUPER_ADMIN = 'super_admin'
    CITY_ADMIN = 'city_admin'
    ANALYST = 'analyst'
    VIEWER = 'viewer'


@dataclass(frozen=True)
class User:
    id: UUID
    name: str
    email: str
    role: str
    password: str | None = None
    city_id: UUID | None = None
    city: City | None = None
