from pydantic import ValidationError
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app.traffic_incidents.incidents_over_time_usecase import IncidentsOverTimeUseCase
from domain.users.user import Roles
from persist.users.user import UserModel

from .traffic_incidents_dto import IncidentsOverTimeInputDto, IncidentsOverTimeOutputDTO


class IncidentsOverTimeView(APIView):
    def get(self, request: Request) -> Response:
        user = request.user
        if user is None or not isinstance(user, UserModel):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            dto = IncidentsOverTimeInputDto.model_validate(request.query_params.dict())
        except ValidationError as e:
            return Response({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)

        # Override the input with the user's city
        if user.role == Roles.VIEWER.value:
            dto.city_id = user.city.id

        from src.core.injector import injector

        usecase = injector.get(IncidentsOverTimeUseCase)
        res = usecase.execute(dto)

        return Response(
            [IncidentsOverTimeOutputDTO.model_validate(i).model_dump() for i in res],
            status=status.HTTP_200_OK,
        )
