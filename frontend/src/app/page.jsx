
'use client';

import { useState } from 'react';

import FormularioLogin from '../componentes/FormularioLogin';
import FormularioPlano from '../componentes/FormularioPlano';
import ListaPlanos from '../componentes/ListaPlanos';

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function PaginaPrincipal() {
  const [token, setToken] = useState('');
  const [usuario, setUsuario] = useState(null);

  const [planos, setPlanos] = useState([]);
  const [filtro, setFiltro] = useState('Todas');

  const [mensagemSucesso, setMensagemSucesso] = useState('');
  const [erroApi, setErroApi] = useState('');

  const [carregandoPlanos, setCarregandoPlanos] = useState(false);
  const [salvandoPlano, setSalvandoPlano] = useState(false);
  const [excluindoId, setExcluindoId] = useState(null);



  function tratarSessaoExpirada() {
    setToken('');
    setUsuario(null);
    setPlanos([]);
    setMensagemSucesso('');
    setErroApi('Sua sessão expirou. Faça login novamente.');
  }
  // Converte o formato da API para o formato utilizado pelos componentes.
  function mapearPlano(plano) {
    return {
      ...plano,
      habilidadeBncc: plano.habilidade_bncc
    };
  }

  // Busca os planos pertencentes ao usuário autenticado.
  async function buscarPlanos(tokenAcesso) {
    setCarregandoPlanos(true);
    setErroApi('');

    try {
      const resposta = await fetch(`${API_URL}/api/planos/`, {
        headers: {
          Authorization: `Bearer ${tokenAcesso}`
        }
      });

      if (resposta.status === 401) {
        tratarSessaoExpirada();
        return;
      }

      if (!resposta.ok) {
        throw new Error('Não foi possível carregar os planos.');
      }
      const dados = await resposta.json();
      setPlanos(dados.map(mapearPlano));
    } catch (erro) {
      setErroApi(erro.message || 'Erro ao carregar os planos.');
    } finally {
      setCarregandoPlanos(false);
    }
  }

  // Executada quando o login é realizado com sucesso.
  async function handleEntrar(dados) {
    setToken(dados.access_token);
    setUsuario(dados.usuario);
    setMensagemSucesso('Login realizado com sucesso!');

    await buscarPlanos(dados.access_token);
  }

  // Envia um novo plano para a API.
  async function handleAdicionarPlano(novoPlano) {
    setSalvandoPlano(true);
    setErroApi('');

    try {
      const resposta = await fetch(`${API_URL}/api/planos/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          titulo: novoPlano.titulo,
          disciplina: novoPlano.disciplina,
          ano: novoPlano.ano,
          habilidade_bncc: novoPlano.habilidadeBncc,
          objetivo: novoPlano.objetivo,
          metodologia: novoPlano.metodologia,
          criado_por_ia: novoPlano.criado_por_ia
        })
      });

      const dados = await resposta.json();

      if (resposta.status === 401) {
        tratarSessaoExpirada();
        return false;
      }

      if (!resposta.ok) {
        throw new Error(dados.detail || 'Não foi possível salvar o plano.');
      }

      setPlanos((atuais) => [mapearPlano(dados), ...atuais]);
      setMensagemSucesso('Plano de aula salvo com sucesso!');
      return true;
      } catch (erro) {
      if (erro instanceof TypeError) {
        setErroApi('Não foi possível conectar ao servidor. Verifique sua conexão e tente novamente.');
      } else {
        setErroApi(erro.message || 'Erro ao salvar o plano.');
      }

      return false;
    }finally {
      setSalvandoPlano(false);
    }
  }

  // Exclui um plano na API.
async function handleExcluirPlano(idParaRemover) {
  setExcluindoId(idParaRemover);
  setErroApi('');
  setMensagemSucesso('');

  try {
    const resposta = await fetch(
      `${API_URL}/api/planos/${idParaRemover}`,
      {
        method: 'DELETE',
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    );
    if (resposta.status === 401) {
      tratarSessaoExpirada();
      return;
    }

    if (!resposta.ok) {
      throw new Error('Não foi possível excluir o plano.');
    }

    setPlanos((atuais) =>
      atuais.filter((plano) => plano.id !== idParaRemover)
    );

    setMensagemSucesso('Plano removido com sucesso!');
  } catch (erro) {
    if (erro instanceof TypeError) {
      setErroApi('Não foi possível conectar ao servidor. Verifique sua conexão e tente novamente.');
    } else {
      setErroApi(erro.message || 'Erro ao excluir o plano.');
    }
  }finally {
  await new Promise((resolver) => setTimeout(resolver, 500));
  setExcluindoId(null);
}
}

  // Encerra a sessão atual.
  function handleSair() {
    setToken('');
    setUsuario(null);
    setPlanos([]);
    setMensagemSucesso('');
    setErroApi('');
  }

  // Sem token, apresenta somente a tela de login.
  if (!token) {
    return (
      <FormularioLogin
        aoEntrar={handleEntrar}
        erroExterno={erroApi}
      />
    );
  }

  return (
    <div>
      <nav className="navbar navbar-dark bg-primary shadow-sm mb-4">
        <div className="container">
          <span className="navbar-brand fw-bold fs-4">
            PlanoFácil
          </span>

          <div className="d-flex align-items-center gap-3">
            <span className="navbar-text text-white small">
              Olá, {usuario?.nome}
            </span>

            <button
              type="button"
              className="btn btn-sm btn-outline-light"
              onClick={handleSair}
            >
              Sair
            </button>
          </div>
        </div>
      </nav>

      <div className="container pb-5">

        {mensagemSucesso && (
          <div className="alert alert-success" role="alert">
            {mensagemSucesso}
            <button
              type="button"
              className="btn-close float-end"
              onClick={() => setMensagemSucesso('')}
              aria-label="Fechar"
            />
          </div>
        )}

        {erroApi && (
          <div className="alert alert-danger" role="alert">
            {erroApi}
          </div>
        )}

        {carregandoPlanos ? (
          <div className="text-center py-5">
            <div className="spinner-border text-primary" role="status">
              <span className="visually-hidden">Carregando...</span>
            </div>
            <p className="text-muted mt-2">Carregando seus planos...</p>
          </div>
        ) : (
          <div className="row">

            <div className="col-lg-5">
              <FormularioPlano
                aoAdicionarPlano={handleAdicionarPlano}
                token={token}
                carregando={salvandoPlano}
              />
            </div>

            <div className="col-lg-7">
              <ListaPlanos
                planos={planos}
                aoExcluirPlano={handleExcluirPlano}
                filtro={filtro}
                aoMudarFiltro={setFiltro}
                excluindoId={excluindoId}
              />
            </div>

          </div>
        )}
      </div>
    </div>
  );
}
