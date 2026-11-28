from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class EsquemaCriarPlano(BaseModel):
    titulo: str
    disciplina: str
    ano: str
    habilidade_bncc: str
    objetivo: str
    metodologia: str = Field(default="")
    criado_por_ia: bool = Field(default=False)

class EsquemaRespostaPlano(EsquemaCriarPlano):
    model_config = ConfigDict(from_attributes=True)
    id: int
    data_criacao: str

class EsquemaRequisicaoIa(BaseModel):
    disciplina: str
    ano: str
    tema: str

class EsquemaRespostaIa(BaseModel):
    titulo: str
    disciplina: str
    ano: str
    habilidade_bncc: str
    objetivo: str
    metodologia: str
    origem: str

