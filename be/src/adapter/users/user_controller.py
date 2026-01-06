
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app.users.me_usecase import MeUseCase
from src.core.injector import injector
from persist.users.user import UserModel
from adapter.users.user_dto import MeResponseDTO


class UsersView(APIView):
    def get(self, request: Request) -> Response:
        user = request.user
        if not isinstance(user, UserModel):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        usecase = injector.get(MeUseCase)
        currentUser = usecase.execute(user.to_domain_user())
        return Response(
            MeResponseDTO.model_validate(currentUser).model_dump(),
            status=status.HTTP_200_OK,
        )
