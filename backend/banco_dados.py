
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

# Carrega as variáveis de ambiente do backend
diretorio_backend = Path(__file__).resolve().parent
load_dotenv(diretorio_backend / ".env")

# Obtém a URL de conexão
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não configurada no ambiente.")

# Utiliza o driver psycopg 3
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )
elif DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql+psycopg://",
        1
    )

# Cria o mecanismo de conexão com o banco
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)


def obter_sessao():
    """Fornece uma sessão do banco para cada requisição."""
    with Session(engine) as sessao:
        yield sessao




from modelos import SQLModel


def criar_tabelas():
    """Cria as tabelas definidas nos modelos, caso ainda não existam."""
    SQLModel.metadata.create_all(engine)
