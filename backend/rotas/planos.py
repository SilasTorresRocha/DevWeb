from fastapi import APIRouter, HTTPException, status
from typing import List
from esquemas.plano import EsquemaCriarPlano, EsquemaRespostaPlano
from banco_memoria import obter_todos_os_planos, adicionar_plano, excluir_plano_por_id

roteador = APIRouter()

@roteador.get("/", response_model=List[EsquemaRespostaPlano])
def listar_planos():
    return obter_todos_os_planos()

@roteador.post("/", response_model=EsquemaRespostaPlano, status_code=status.HTTP_201_CREATED)
def criar_plano(dados: EsquemaCriarPlano):
    novo_plano = adicionar_plano(dados.model_dump())
    return novo_plano

@roteador.delete("/{plano_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_plano(plano_id: int):
    sucesso = excluir_plano_por_id(plano_id)
    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Plano com ID {plano_id} não encontrado."
        )
    return None

