from fastapi import APIRouter
from esquemas.plano import EsquemaRequisicaoIa, EsquemaRespostaIa
from servicos.servico_ia import gerar_sugestao_com_ia

roteador = APIRouter()

@roteador.post("/gerar-plano", response_model=EsquemaRespostaIa)
def gerar_plano_com_ia(requisicao: EsquemaRequisicaoIa):
    resultado = gerar_sugestao_com_ia(
        disciplina=requisicao.disciplina,
        ano=requisicao.ano,
        tema=requisicao.tema
    )
    return resultado

