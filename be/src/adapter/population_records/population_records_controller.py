from pydantic import ValidationError
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app.population_records.growth_over_time_usecase import GrowthOverTimeUseCase
from domain.users.user import Roles
from persist.users.user import UserModel

from .population_records_dto import GrowthOverTimeInputDto, GrowthOverTimeOutputDTO


class PopulationRecordsGrowthOverTimeView(APIView):
    def get(self, request: Request) -> Response:
        user = request.user
        if user is None or not isinstance(user, UserModel):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            dto = GrowthOverTimeInputDto.model_validate(request.query_params.dict())
        except ValidationError as e:
            return Response({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)

        # Override the input with the user's city
        if user.role == Roles.VIEWER.value:
            dto.city_id = user.city.id

        from src.core.injector import injector

        usecase = injector.get(GrowthOverTimeUseCase)
        res = usecase.execute(dto)

        return Response(
            [GrowthOverTimeOutputDTO.model_validate(i).model_dump() for i in res],
            status=status.HTTP_200_OK,
        )
