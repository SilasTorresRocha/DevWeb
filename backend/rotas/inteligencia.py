from fastapi import APIRouter
from esquemas.plano import EsquemaRequisicaoIa, EsquemaRespostaIa
from servicos.servico_ia import gerar_sugestao_com_ia

roteador = APIRouter()

@roteador.post("/gerar-plano", response_model=EsquemaRespostaIa, summary="Gerar sugestão de plano com IA")
def gerar_plano_com_ia(requisicao: EsquemaRequisicaoIa):
    """
    Recebe disciplina, ano e tema, e consulta a IA para sugerir
    automaticamente a habilidade BNCC e o roteiro metodológico da aula.
    Possui cache e sistema de contingência anti-falha.
    """
    resultado = gerar_sugestao_com_ia(
        disciplina=requisicao.disciplina,
        ano=requisicao.ano,
        tema=requisicao.tema
    )
    return resultado

