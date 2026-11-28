
'use client';

import { useState } from 'react';

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function FormularioLogin({ aoEntrar, erroExterno = '' }) {
  const [modoCadastro, setModoCadastro] = useState(false);

  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');

  const [carregando, setCarregando] = useState(false);
  const [erro, setErro] = useState('');

  async function handleSubmit(evento) {
    evento.preventDefault();
    setErro('');
    setCarregando(true);

    const endpoint = modoCadastro ? '/api/auth/cadastro' : '/api/auth/login';
    const corpo = modoCadastro
      ? { nome, email, senha }
      : { email, senha };

    try {
      const resposta = await fetch(`${API_URL}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(corpo)
      });

      const dados = await resposta.json().catch(() => ({}));

      if (!resposta.ok) {
        let mensagemErro;

        if (Array.isArray(dados.detail)) {
          mensagemErro = dados.detail
            .map((erro) => erro.msg)
            .join('. ');
        } else {
          mensagemErro = dados.detail;
        }

        throw new Error(
          mensagemErro || 'Não foi possível realizar a operação.'
        );
      }

      await aoEntrar(dados);
    } catch (erro) {
      if (erro instanceof TypeError) {
        setErro('Não foi possível conectar ao servidor. Verifique sua conexão e tente novamente.');
      } else {
        setErro(erro.message || 'Erro ao realizar a operação.');
      }
    }finally {
      setCarregando(false);
    }
  }

  function alternarModo() {
    setModoCadastro(!modoCadastro);
    setErro('');
  }

  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-md-6 col-lg-4">
          <div className="card shadow-sm">
            <div className="card-body p-4">
              <h3 className="text-center fw-bold mb-2">
                PlanoFácil
              </h3>

              <p className="text-center text-muted mb-4">
                {modoCadastro
                  ? 'Crie sua conta para começar a planejar suas aulas.'
                  : 'Entre para acessar seus planos de aula.'}
              </p>

              {(erro || erroExterno) && (
                <div className="alert alert-danger" role="alert">
                  {erroExterno || erro}
                </div>
              )}

              <form onSubmit={handleSubmit}>
                {modoCadastro && (
                  <div className="mb-3">
                    <label className="form-label fw-semibold">
                      Nome completo
                    </label>

                    <input
                      type="text"
                      className="form-control"
                      value={nome}
                      onChange={(e) => setNome(e.target.value)}
                      minLength={2}
                      maxLength={100}
                      required
                    />
                  </div>
                )}

                <div className="mb-3">
                  <label className="form-label fw-semibold">
                    E-mail
                  </label>

                  <input
                    type="email"
                    className="form-control"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                  />
                </div>

                <div className="mb-3">
                  <label className="form-label fw-semibold">
                    Senha
                  </label>

                  <input
                    type="password"
                    className="form-control"
                    value={senha}
                    onChange={(e) => setSenha(e.target.value)}
                    minLength={8}
                    maxLength={128}
                    required
                  />

                  {modoCadastro && (
                    <small className="text-muted">
                      A senha deve ter pelo menos 8 caracteres.
                    </small>
                  )}
                </div>

                <button
                  type="submit"
                  className="btn btn-primary w-100"
                  disabled={carregando}
                >
                  {carregando
                    ? 'Aguarde...'
                    : modoCadastro
                      ? 'Criar conta'
                      : 'Entrar'}
                </button>
              </form>

              <hr />

              <p className="text-center mb-0">
                {modoCadastro
                  ? 'Já possui uma conta?'
                  : 'Ainda não possui uma conta?'}
              </p>

              <button
                type="button"
                className="btn btn-link w-100 text-decoration-none"
                onClick={alternarModo}
                disabled={carregando}
              >
                {modoCadastro ? 'Fazer login' : 'Criar uma conta'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
