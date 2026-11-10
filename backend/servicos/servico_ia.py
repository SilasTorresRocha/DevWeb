import os
import json
import time
import httpx
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

CHAVE_API = os.getenv("CHAVE_API_GEMINI", "").strip()
URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

# Cache em memória para evitar gastar cota em requisições repetidas
CACHE_CONSULTAS = {}

# Controle simples de tempo para evitar rajada de requisições
ULTIMA_REQUISICAO = 0
INTERVALO_MINIMO_SEGUNDOS = 3.0

def plano_fallback(disciplina: str, ano: str, tema: str) -> dict:
    """
    Plano de contingência.
    Garante que a apresentacao nao trave caso a internet oscile ou a cota esgote.
    """
    habilidades_exemplo = {
        "Matemática": "EF06MA17 - Reconhecer e identificar figuras espaciais (prismas, pirâmides) e suas planificações no cotidiano.",
        "Língua Portuguesa": "EF08LP05 - Analisar e produzir textos argumentativos e de opinião explorando recursos de síntese e coesão.",
        "Ciências": "EF07CI08 - Avaliar alterações provocadas por ações humanas em ecossistemas e cadeias alimentares locais.",
        "História": "EF09HI05 - Analisar os processos de transformação social e cidadania no período republicano brasileiro.",
        "Geografia": "EF07GE06 - Discutir a dinâmica populacional e os fluxos migratórios em diferentes regiões brasileiras."
    }

    habilidade = habilidades_exemplo.get(
        disciplina, 
        f"BNCC-{disciplina[:3].upper()} - Desenvolver habilidades essenciais e aplicadas ao tema {tema} no {ano}."
    )

    return {
        "titulo": f"Aula Prática: {tema}",
        "disciplina": disciplina,
        "ano": ano,
        "habilidade_bncc": habilidade,
        "objetivo": f"Compreender e aplicar os conceitos fundamentais de {tema} através de situações contextualizadas à realidade dos estudantes.",
        "metodologia": f"1. Acolhimento e problematização inicial sobre {tema} (10 min).\n2. Atividade prática orientada em pequenos grupos (25 min).\n3. Compartilhamento das soluções no quadro e fechamento pedagógico (15 min).",
        "origem": "contingencia_segura (anti-falha)"
    }

def gerar_sugestao_com_ia(disciplina: str, ano: str, tema: str) -> dict:
    """
    Chama a API do Google Gemini via requisição HTTP POST direta (REST),
    utilizando cache em memória e plano de contingência automático.
    """
    global ULTIMA_REQUISICAO

    chave_cache = f"{disciplina}_{ano}_{tema}".strip().lower()

    # Verifica se já está em cache
    if chave_cache in CACHE_CONSULTAS:
        resultado = CACHE_CONSULTAS[chave_cache].copy()
        resultado["origem"] = "cache_memoria (economia de cota)"
        return resultado

    # Se não houver chave configurada, usa o fallback imediato
    if not CHAVE_API or CHAVE_API.startswith("sua_chave"):
        return plano_fallback(disciplina, ano, tema)

    # Controle de intervalo rate limit
    tempo_atual = time.time()
    if tempo_atual - ULTIMA_REQUISICAO < INTERVALO_MINIMO_SEGUNDOS:
        time.sleep(INTERVALO_MINIMO_SEGUNDOS - (tempo_atual - ULTIMA_REQUISICAO))
    ULTIMA_REQUISICAO = time.time()

    # Prompt estruturado exigindo JSON direto
    prompt = f"""
Você é um especialista em educação básica brasileira e na BNCC (Base Nacional Comum Curricular).
Crie um plano de aula conciso e realista para:
- Disciplina: {disciplina}
- Ano escolar: {ano}
- Tema: {tema}

Responda ESTRITAMENTE em formato JSON puro, sem blocos de código adicionais, com o seguinte formato:
{{
  "titulo": "Título criativo e claro da aula",
  "habilidade_bncc": "Código oficial e descrição da habilidade BNCC (ex: EF06MA07 - ...)",
  "objetivo": "Objetivo de aprendizagem claro em 1 ou 2 frases",
  "metodologia": "Passo a passo da aula de 50 minutos com minutagem estimada"
}}
"""

    cabecalhos = {
        "Content-Type": "application/json",
        "X-goog-api-key": CHAVE_API
    }

    corpo = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        # Faz a chamada REST para o Gemini
        with httpx.Client(timeout=10.0) as cliente:
            resposta = cliente.post(URL_GEMINI, headers=cabecalhos, json=corpo)

        if resposta.status_code == 200:
            dados = resposta.json()
            texto_gerado = dados["candidates"][0]["content"]["parts"][0]["text"].strip()

            # Remove marcações de markdown ```json
            if texto_gerado.startswith("```"):
                linhas = texto_gerado.split("\n")
                if linhas[0].startswith("```"):
                    linhas = linhas[1:]
                if linhas and linhas[-1].startswith("```"):
                    linhas = linhas[:-1]
                texto_gerado = "\n".join(linhas).strip()

            json_ia = json.loads(texto_gerado)

            resultado = {
                "titulo": json_ia.get("titulo", f"Aula: {tema}"),
                "disciplina": disciplina,
                "ano": ano,
                "habilidade_bncc": json_ia.get("habilidade_bncc", "Habilidade BNCC a ser alinhada."),
                "objetivo": json_ia.get("objetivo", f"Compreender os aspectos centrais de {tema}."),
                "metodologia": json_ia.get("metodologia", "Atividades didáticas a definir."),
                "origem": "api_gemini_ao_vivo"
            }

            # Salva no cache
            CACHE_CONSULTAS[chave_cache] = resultado
            return resultado

        else:
            # Em caso de erro na API do Google (429 cota, 400, etc.), usa o plano de contingência
            return plano_fallback(disciplina, ano, tema)

    except Exception:
        # Qualquer falha de rede/timeout ativa o fallback seguro
        return plano_fallback(disciplina, ano, tema)

