
from datetime import datetime
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from esquemas.plano import EsquemaCriarPlano, EsquemaRespostaPlano

from sqlmodel import Session, select
from banco_dados import obter_sessao
from modelos import Plano

from rotas.autenticacao import obter_usuario_atual

roteador = APIRouter()


@roteador.get("/", response_model=List[EsquemaRespostaPlano])
def listar_planos(
    usuario = Depends(obter_usuario_atual),
    sessao: Session = Depends(obter_sessao)
):
    """Lista somente os planos do usuário autenticado."""

    return sessao.exec(
        select(Plano).where(Plano.usuario_id == usuario.id)
    ).all()



@roteador.post(
    "/",
    response_model=EsquemaRespostaPlano,
    status_code=status.HTTP_201_CREATED
)
def criar_plano(
    dados: EsquemaCriarPlano,
    usuario = Depends(obter_usuario_atual),
    sessao: Session = Depends(obter_sessao)
):
    """Cria um plano vinculado ao usuário autenticado."""

    novo_plano = Plano(
        **dados.model_dump(),
        usuario_id=usuario.id,
        data_criacao=datetime.now().strftime("%d/%m/%Y")
    )

    sessao.add(novo_plano)
    sessao.commit()
    sessao.refresh(novo_plano)

    return novo_plano


@roteador.delete("/{plano_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_plano(
    plano_id: int,
    usuario = Depends(obter_usuario_atual),
    sessao: Session = Depends(obter_sessao)
):
    """Remove somente planos pertencentes ao usuário autenticado."""

    plano = sessao.exec(
        select(Plano).where(
            Plano.id == plano_id,
            Plano.usuario_id == usuario.id
        )
    ).first()

    if plano is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plano não encontrado ou não pertence ao usuário."
        )

    sessao.delete(plano)
    sessao.commit()

    return None
