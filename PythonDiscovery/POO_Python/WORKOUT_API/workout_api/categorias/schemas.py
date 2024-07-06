from typing import Annotated
from pydantic.fields import Field
from workout_api.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", example="Scale", max_length=10)]