import os
import json
import time
import httpx
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (pasta backend ou raiz)
diretorio_backend = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(diretorio_backend, ".env"))
load_dotenv(os.path.join(os.path.dirname(diretorio_backend), ".env"))
load_dotenv()

CHAVE_API = os.getenv("CHAVE_API_GEMINI", "").strip()
MODELOS_TENTATIVA = [
    "gemini-3.5-flash-lite",
    "gemini-3.8-flash",
    "gemini-flash-latest"
]
TEMPO_LIMITE_TIMEOUT_SEGUNDOS = 30.0

# Cache em memória para evitar gastar cota em requisições repetidas
CACHE_CONSULTAS = {}

# Controle simples de tempo para evitar rajada de requisições
ULTIMA_REQUISICAO = 0
INTERVALO_MINIMO_SEGUNDOS = 3.0

def plano_fallback(disciplina: str, ano: str, tema: str) -> dict:
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
    global ULTIMA_REQUISICAO

    chave_cache = f"{disciplina}_{ano}_{tema}".strip().lower()

    # Verifica se já está em cache
    if chave_cache in CACHE_CONSULTAS:
        resultado = CACHE_CONSULTAS[chave_cache].copy()
        resultado["origem"] = "cache_memoria (economia de cota)"
        return resultado

    # Recarrega a chave dinamicamente caso o arquivo .env tenha sido criado ou editado recentemente
    chave_atual = os.getenv("CHAVE_API_GEMINI", CHAVE_API).strip()

    # Se não houver chave configurada, usa o fallback imediato
    if not chave_atual or chave_atual.startswith("sua_chave"):
        print("[IA AVISO] Nenhuma chave CHAVE_API_GEMINI encontrada no .env. Ativando plano de contingência.")
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
        "X-goog-api-key": chave_atual
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

    # Tenta os modelos disponíveis
    for modelo in MODELOS_TENTATIVA:
        url_gemini = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={chave_atual}"
        try:
            print(f"[IA INFO] Tentando chamada ao Google Gemini (Modelo: {modelo}, timeout: {TEMPO_LIMITE_TIMEOUT_SEGUNDOS}s)...")
            with httpx.Client(timeout=TEMPO_LIMITE_TIMEOUT_SEGUNDOS) as cliente:
                resposta = cliente.post(url_gemini, headers=cabecalhos, json=corpo)

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
                print(f"[IA SUCESSO] Plano gerado pelo modelo {modelo} com sucesso!")
                return resultado

            else:
                print(f"[IA ERRO] Modelo {modelo} retornou HTTP {resposta.status_code}: {resposta.text[:300]}")
                # Se for indisponibilidade temporária (503/429/500) ou modelo não encontrado (404), tenta o próximo modelo
                if resposta.status_code in (404, 429, 500, 502, 503, 504):
                    time.sleep(1.0)
                    continue
                # Se for erro definitivo (chave inválida 401/403 ou requisição malformada 400), não adianta tentar outros
                break

        except Exception as erro:
            print(f"[IA ERRO] Exceção ao chamar modelo {modelo}: {erro}")
            continue

    # Se todas as tentativas falharem, aciona o fallback seguro para não quebrar a aplicação
    print("[IA AVISO] Usando plano_fallback (contingência segura).")
    return plano_fallback(disciplina, ano, tema)

