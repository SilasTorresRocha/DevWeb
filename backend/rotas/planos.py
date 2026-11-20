
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from esquemas.plano import EsquemaCriarPlano, EsquemaRespostaPlano

from banco_memoria import (
    obter_todos_os_planos,
    adicionar_plano,
    excluir_plano_por_id
)

from rotas.autenticacao import obter_usuario_atual

roteador = APIRouter()


@roteador.get("/", response_model=List[EsquemaRespostaPlano])
def listar_planos(usuario: dict = Depends(obter_usuario_atual)):
    """Lista os planos públicos e os do usuário autenticado."""
    return obter_todos_os_planos(usuario["id"])


@roteador.post(
    "/",
    response_model=EsquemaRespostaPlano,
    status_code=status.HTTP_201_CREATED
)
def criar_plano(
    dados: EsquemaCriarPlano,
    usuario: dict = Depends(obter_usuario_atual)
):
    """Cria um plano vinculado ao usuário autenticado."""
    novo_plano = adicionar_plano(
        dados.model_dump(),
        usuario["id"]
    )

    return novo_plano


@roteador.delete("/{plano_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_plano(
    plano_id: int,
    usuario: dict = Depends(obter_usuario_atual)
):
    """Remove somente planos pertencentes ao usuário."""
    sucesso = excluir_plano_por_id(
        plano_id,
        usuario["id"]
    )

    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plano não encontrado ou não pertence ao usuário."
        )

    return None
