
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

from esquemas.usuario import (
    EsquemaCriarUsuario,
    EsquemaLogin,
    EsquemaRespostaToken
)

from sqlmodel import Session, select
from banco_dados import obter_sessao
from modelos import Usuario


from seguranca import (
    gerar_hash_senha,
    verificar_senha,
    criar_token_acesso,
    verificar_token
)

roteador = APIRouter()

# Extrai o token enviado no cabeçalho Authorization
esquema_seguranca = HTTPBearer(auto_error=False)


def montar_resposta_autenticacao(usuario: dict):
    """Gera o token e prepara a resposta pública do usuário."""

    token = criar_token_acesso({
        "sub": str(usuario["id"])
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "usuario": {
            "id": usuario["id"],
            "nome": usuario["nome"],
            "email": usuario["email"]
        }
    }


@roteador.post(
    "/cadastro",
    response_model=EsquemaRespostaToken,
    status_code=status.HTTP_201_CREATED
)

@roteador.post(
    "/cadastro",
    response_model=EsquemaRespostaToken,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_usuario(
    dados: EsquemaCriarUsuario,
    sessao: Session = Depends(obter_sessao)
):
    """Cadastra um usuário no PostgreSQL e retorna seu token."""

    usuario_existente = sessao.exec(
        select(Usuario).where(Usuario.email == dados.email)
    ).first()

    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Este e-mail já está cadastrado."
        )

    usuario = Usuario(
        nome=dados.nome,
        email=dados.email,
        senha_hash=gerar_hash_senha(dados.senha)
    )

    sessao.add(usuario)
    sessao.commit()
    sessao.refresh(usuario)

    return montar_resposta_autenticacao({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email
    })


@roteador.post(
    "/login",
    response_model=EsquemaRespostaToken
)
def realizar_login(
    dados: EsquemaLogin,
    sessao: Session = Depends(obter_sessao)
):
    """Valida as credenciais no PostgreSQL e retorna um JWT."""

    usuario = sessao.exec(
        select(Usuario).where(Usuario.email == dados.email)
    ).first()

    if not usuario or not verificar_senha(
        dados.senha,
        usuario.senha_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return montar_resposta_autenticacao({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email
    })



def obter_usuario_atual(
    credenciais: HTTPAuthorizationCredentials = Depends(esquema_seguranca),
    sessao: Session = Depends(obter_sessao)
):
    """Valida o JWT e retorna o usuário autenticado do PostgreSQL."""

    if credenciais is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticação não informado.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    try:
        conteudo_token = verificar_token(credenciais.credentials)
        usuario_id = int(conteudo_token["sub"])

    except (jwt.InvalidTokenError, KeyError, TypeError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    usuario = sessao.get(Usuario, usuario_id)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return usuario
