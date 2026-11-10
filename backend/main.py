import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Carrega configurações do arquivo .env
load_dotenv()

from rotas.planos import roteador as roteador_planos
from rotas.inteligencia import roteador as roteador_ia

"""
Projeto: PlanoFácil - Apoio ao Planejamento Docente com IA
"""

app = FastAPI(
    title="PlanoFácil API",
    description="API RESTful modular para apoio ao planejamento docente na Educação Básica com Inteligência Artificial (Ideia 8).",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuração de CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(roteador_planos, prefix="/api/planos", tags=["Planos de Aula"])
app.include_router(roteador_ia, prefix="/api/ia", tags=["Inteligência Artificial"])

@app.get("/", tags=["Status"])
def verificar_status():
    """Rota raiz para verificação rápida de funcionamento da API."""
    return {
        "sistema": "PlanoFácil API",
        "status": "operacional",
        "versao": "1.0.0",
        "documentacao_swagger": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    porta = int(os.getenv("PORTA", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=porta, reload=True)

