import uuid
from typing import Any

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from domain.users.user import User
from domain.users.user import Roles
from ..cities.city import City
from ..cities.city import CityModel


class UserManager(BaseUserManager["UserModel"]):
    def create_superuser(self, email: str, name: str, password: str, **_) -> "UserModel":
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)

        user.role = Roles.SUPER_ADMIN.value
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class UserModel(AbstractUser):

    id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4
    )  # type: ignore[assignment]
    name: str = models.CharField(max_length=255)  # type: ignore[assignment]
    email: str = models.EmailField(  # type: ignore[assignment]
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    role: str = models.CharField(  # type: ignore[assignment]
        choices=[(role.value, role.value) for role in Roles],
        default=Roles.VIEWER.value,
    )
    city: City = models.ForeignKey(
        # type: ignore[assignment]
        CityModel, blank=True, null=True, on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", 'role']

    objects: Any = UserManager()  # type: ignore[misc]

    def __str__(self) -> str:
        return str(self.email)

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["id"]

    def to_domain(self) -> User:
        return User(
            id=self.id,
            name=self.name,
            email=self.email,
            role=self.role,
            city=self.city,
            city_id=self.city.id,
        )
