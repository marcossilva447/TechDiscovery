from pydantic import BaseModel

class AtletaSchema(BaseModel):
    nome: Annotated[str, Field(description="Nome do atleta", example="João da Silva", max_length=50)] # type: ignore
    cpf: Annotated[str, Field(description="CPF do atleta", example="123.456.789-00", max_length=11)] # type: ignore
    idade: Annotated[int, Field(description="Idade do atleta", example=25)] # type: ignore
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=75.5)] # type: ignore
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=1.75)] # type: ignore
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)] # type: ignore
    
