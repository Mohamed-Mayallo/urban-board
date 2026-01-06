from pydantic import BaseModel, UUID4, ConfigDict


class MeResponseDTO(BaseModel):
    id: UUID4
    name: str
    email: str
    role: str

    model_config = ConfigDict(from_attributes=True)
