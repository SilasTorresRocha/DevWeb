
import os
import jwt

from pathlib import Path
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from pwdlib import PasswordHash

# Carrega as variáveis do arquivo .env do backend
diretorio_backend = Path(__file__).resolve().parent
load_dotenv(diretorio_backend / ".env")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

gerenciador_senhas = PasswordHash.recommended()


def obter_chave_secreta() -> str:
    """Obtém a chave secreta configurada no ambiente."""
    chave = os.getenv("SECRET_KEY")

    if not chave:
        raise RuntimeError("SECRET_KEY não configurada no ambiente.")

    return chave


def gerar_hash_senha(senha: str) -> str:
    """Gera um hash seguro para armazenar a senha."""
    return gerenciador_senhas.hash(senha)


def verificar_senha(senha: str, senha_hash: str) -> bool:
    """Verifica se a senha corresponde ao hash armazenado."""
    return gerenciador_senhas.verify(senha, senha_hash)


def criar_token_acesso(dados: dict) -> str:
    """Cria um token JWT com validade de 60 minutos."""
    dados_token = dados.copy()

    expiracao = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    dados_token.update({"exp": expiracao})

    return jwt.encode(
        dados_token,
        obter_chave_secreta(),
        algorithm=ALGORITHM
    )


def verificar_token(token: str) -> dict:
    """Valida o JWT e retorna seu conteúdo."""
    return jwt.decode(
        token,
        obter_chave_secreta(),
        algorithms=[ALGORITHM]
    )
