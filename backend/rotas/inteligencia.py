
from fastapi import APIRouter, Depends

from esquemas.plano import (
    EsquemaRequisicaoIa,
    EsquemaRespostaIa
)

from servicos.servico_ia import gerar_sugestao_com_ia
from rotas.autenticacao import obter_usuario_atual

roteador = APIRouter()


@roteador.post(
    "/gerar-plano",
    response_model=EsquemaRespostaIa
)
def gerar_plano_com_ia(
    requisicao: EsquemaRequisicaoIa,
    usuario: dict = Depends(obter_usuario_atual)
):
    """Gera uma sugestão de plano para o usuário autenticado."""

    resultado = gerar_sugestao_com_ia(
        disciplina=requisicao.disciplina,
        ano=requisicao.ano,
        tema=requisicao.tema
    )

    return resultado
