from pydantic import BaseModel, Field
from typing import Optional

"""
Modelos Pydantic para validação de dados da API.
"""

class EsquemaCriarPlano(BaseModel):
    titulo: str = Field(..., description="Título da aula", example="Introdução a Frações")
    disciplina: str = Field(..., description="Componente curricular", example="Matemática")
    ano: str = Field(..., description="Ano escolar da turma", example="6º Ano")
    habilidade_bncc: str = Field(..., description="Código ou descrição da BNCC", example="EF06MA07 - Compreender frações...")
    objetivo: str = Field(..., description="Objetivo geral de aprendizagem", example="Compreender o conceito de fração.")
    metodologia: Optional[str] = Field("", description="Passo a passo didático da aula")
    criado_por_ia: Optional[bool] = Field(False, description="Indica se foi sugerido por IA")

class EsquemaRespostaPlano(EsquemaCriarPlano):
    id: int = Field(..., description="Identificador único do plano")
    data_criacao: str = Field(..., description="Data de criação no formato DD/MM/AAAA")

class EsquemaRequisicaoIa(BaseModel):
    disciplina: str = Field(..., description="Disciplina escolar", example="Matemática")
    ano: str = Field(..., description="Ano ou etapa escolar", example="6º Ano")
    tema: str = Field(..., description="Tema ou assunto que o professor quer lecionar", example="Frações e Divisão no Cotidiano")

class EsquemaRespostaIa(BaseModel):
    titulo: str
    disciplina: str
    ano: str
    habilidade_bncc: str
    objetivo: str
    metodologia: str
    origem: str = Field(..., description="Indica se a resposta veio da API ao vivo ou do cache/fallback")

