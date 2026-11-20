
from pydantic import BaseModel, Field, field_validator


class EsquemaCriarUsuario(BaseModel):
    nome: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=5, max_length=150)
    senha: str = Field(min_length=8, max_length=128)

    @field_validator("email")
    @classmethod
    def normalizar_email(cls, valor: str) -> str:
        return valor.strip().lower()

    @field_validator("nome")
    @classmethod
    def normalizar_nome(cls, valor: str) -> str:
        return valor.strip()


class EsquemaLogin(BaseModel):
    email: str
    senha: str

    @field_validator("email")
    @classmethod
    def normalizar_email(cls, valor: str) -> str:
        return valor.strip().lower()


class EsquemaRespostaUsuario(BaseModel):
    id: int
    nome: str
    email: str


class EsquemaRespostaToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
    usuario: EsquemaRespostaUsuario
