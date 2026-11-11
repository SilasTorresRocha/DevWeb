from pydantic import BaseModel
from typing import Optional

class EsquemaCriarPlano(BaseModel):
    titulo: str
    disciplina: str
    ano: str
    habilidade_bncc: str
    objetivo: str
    metodologia: Optional[str] = ""
    criado_por_ia: Optional[bool] = False

class EsquemaRespostaPlano(EsquemaCriarPlano):
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

