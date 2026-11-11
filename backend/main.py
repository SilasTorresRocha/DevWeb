import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

diretorio_backend = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(diretorio_backend, ".env"))
load_dotenv(os.path.join(os.path.dirname(diretorio_backend), ".env"))
load_dotenv()

from rotas.planos import roteador as roteador_planos
from rotas.inteligencia import roteador as roteador_ia

VERSAO_API = "1.2.0"

app = FastAPI(
    title="PlanoFácil",
    version=VERSAO_API
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(roteador_planos, prefix="/api/planos", tags=["Planos"])
app.include_router(roteador_ia, prefix="/api/ia", tags=["IA"])

# Rota fixa de verificação de status
@app.get("/status", tags=["Status"])
def status():
    return {
        "status": "ok",
        "versao": VERSAO_API
    }

# Carrega o Easter Egg  
caminho_easter = os.path.join(diretorio_backend, "easter_egg")
if os.path.exists(caminho_easter):
    try:
        from fastapi.staticfiles import StaticFiles
        from easter_egg.roteador import roteador as roteador_easter
        app.mount("/easter_egg", StaticFiles(directory=caminho_easter), name="arquivos_easter_egg")
        app.include_router(roteador_easter)
    except Exception as erro:
        print(f"[EASTER EGG] Aviso: {erro}")
else:
    # Se a pasta não existir (clone limpo do GitHub), a raiz responde com o status padrão
    @app.get("/", tags=["Status"])
    def status_raiz():
        return {
            "status": "ok",
            "versao": VERSAO_API
        }

if __name__ == "__main__":
    import uvicorn
    porta = int(os.getenv("PORTA", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=porta, reload=True)

