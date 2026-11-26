
from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100)
    email: str = Field(max_length=150, unique=True, index=True)
    senha_hash: str = Field(max_length=255)

    # Um usuário pode possuir vários planos
    planos: List["Plano"] = Relationship(back_populates="usuario")


class Plano(SQLModel, table=True):
    __tablename__ = "plano"

    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    disciplina: str
    ano: str
    habilidade_bncc: str
    objetivo: str
    metodologia: str = Field(default="")
    criado_por_ia: bool = Field(default=False)
    data_criacao: str

    # Todo plano pertence obrigatoriamente a um usuário
    usuario_id: int = Field(
        foreign_key="usuario.id",
        index=True
    )

    usuario: Optional[Usuario] = Relationship(back_populates="planos")
