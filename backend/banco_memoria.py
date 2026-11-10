from datetime import datetime

"""
Banco de dados em memória para a Sprint 2.
"""

BANCO_PLANOS = [
    {
        "id": 1,
        "titulo": "Introdução a Frações com Exemplos Cotidianos",
        "disciplina": "Matemática",
        "ano": "6º Ano",
        "habilidade_bncc": "EF06MA07 - Compreender e comparar frações como parte de um todo.",
        "objetivo": "Compreender o conceito de fração através de divisão em partes iguais.",
        "metodologia": "1. Pergunta disparadora com divisão de alimentos (15 min). 2. Exercícios práticos (25 min). 3. Síntese no quadro (10 min).",
        "criado_por_ia": True,
        "data_criacao": "04/11/2026"
    },
    {
        "id": 2,
        "titulo": "Análise Crítica de Notícias e Fake News",
        "disciplina": "Língua Portuguesa",
        "ano": "8º Ano",
        "habilidade_bncc": "EF08LP03 - Analisar textos de opinião e checagem de fatos.",
        "objetivo": "Diferenciar fatos de boatos em publicações de redes sociais.",
        "metodologia": "1. Leitura de manchetes reais (15 min). 2. Discussão em grupo sobre fontes (25 min). 3. Conclusão da turma (10 min).",
        "criado_por_ia": False,
        "data_criacao": "03/11/2026"
    },
    {
        "id": 3,
        "titulo": "Cadeia Alimentar e Equilíbrio Ecológico",
        "disciplina": "Ciências",
        "ano": "7º Ano",
        "habilidade_bncc": "EF07CI08 - Avaliar alterações provocadas em cadeias alimentares.",
        "objetivo": "Identificar produtores, consumidores e decompositores em ecossistemas locais.",
        "metodologia": "1. Desenho da teia ecológica (20 min). 2. Debate sobre desequilíbrios (20 min). 3. Fechamento (10 min).",
        "criado_por_ia": True,
        "data_criacao": "02/11/2026"
    }
]

def obter_todos_os_planos():
    return BANCO_PLANOS

def adicionar_plano(dados_plano: dict):
    # Gera um novo ID baseado no maior ID existente
    novo_id = max([p["id"] for p in BANCO_PLANOS], default=0) + 1
    plano_completo = {
        **dados_plano,
        "id": novo_id,
        "criado_por_ia": dados_plano.get("criado_por_ia", False),
        "data_criacao": datetime.now().strftime("%d/%m/%Y")
    }
    BANCO_PLANOS.insert(0, plano_completo)
    return plano_completo

def excluir_plano_por_id(plano_id: int):
    global BANCO_PLANOS
    tamanho_antes = len(BANCO_PLANOS)
    BANCO_PLANOS = [p for p in BANCO_PLANOS if p["id"] != plano_id]
    return len(BANCO_PLANOS) < tamanho_antes

