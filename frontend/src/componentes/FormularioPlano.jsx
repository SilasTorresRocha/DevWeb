
'use client';

import { useState } from 'react';

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function FormularioPlano({
  aoAdicionarPlano,
  token,
  carregando = false
}) {
  const [titulo, setTitulo] = useState('');
  const [disciplina, setDisciplina] = useState('Matemática');
  const [ano, setAno] = useState('6º Ano');
  const [habilidadeBncc, setHabilidadeBncc] = useState('');
  const [objetivo, setObjetivo] = useState('');
  const [metodologia, setMetodologia] = useState('');

  const [tema, setTema] = useState('');
  const [carregandoIa, setCarregandoIa] = useState(false);
  const [erroIa, setErroIa] = useState('');

  async function handlePreencherComIa() {
    if (!tema.trim()) {
      setErroIa('Informe um tema para gerar o plano com IA.');
      return;
    }

    setErroIa('');
    setCarregandoIa(true);

    try {
      const resposta = await fetch(`${API_URL}/api/ia/gerar-plano`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          disciplina,
          ano,
          tema
        })
      });

      const dados = await resposta.json().catch(() => ({}));

      if (!resposta.ok) {
        throw new Error(
          dados.detail || 'Não foi possível gerar o plano com IA. Tente novamente.'
        );
      }

      setTitulo(dados.titulo);
      setDisciplina(dados.disciplina);
      setAno(dados.ano);
      setHabilidadeBncc(dados.habilidade_bncc);
      setObjetivo(dados.objetivo);
      setMetodologia(dados.metodologia);
    } catch (erro) {
      if (erro instanceof TypeError) {
        setErroIa('Não foi possível conectar ao servidor. Verifique sua conexão e tente novamente.');
      } else {
        setErroIa(erro.message || 'Erro ao gerar o plano com inteligência artificial.');
      }
    }finally {
      setCarregandoIa(false);
    }
  }

  async function handleSubmit(evento) {
    evento.preventDefault();

    if (!titulo.trim() || !habilidadeBncc.trim()) {
      alert('Por favor, preencha pelo menos o Título e a Habilidade BNCC.');
      return;
    }

    const novoPlano = {
      titulo,
      disciplina,
      ano,
      habilidadeBncc,
      objetivo: objetivo || 'Objetivo a ser definido pelo professor.',
      metodologia: metodologia || 'Metodologia padrão da aula.',
      criado_por_ia: false
    };

    const sucesso = await aoAdicionarPlano(novoPlano);

    if (sucesso) {
      setTitulo('');
      setHabilidadeBncc('');
      setObjetivo('');
      setMetodologia('');
      setTema('');
    }
  }

  return (
    <div className="card shadow-sm mb-4">
      <div className="card-header bg-white d-flex justify-content-between align-items-center">
        <h5 className="mb-0 fw-bold">Novo Plano de Aula</h5>
      </div>

      <div className="card-body">
        <form onSubmit={handleSubmit}>

          <div className="mb-3">
            <label className="form-label fw-semibold">Disciplina</label>
            <select
              className="form-select"
              value={disciplina}
              onChange={(e) => setDisciplina(e.target.value)}
            >
              <option value="Matemática">Matemática</option>
              <option value="Língua Portuguesa">Língua Portuguesa</option>
              <option value="Ciências">Ciências</option>
              <option value="História">História</option>
              <option value="Geografia">Geografia</option>
            </select>
          </div>

          <div className="mb-3">
            <label className="form-label fw-semibold">Ano Escolar</label>
            <select
              className="form-select"
              value={ano}
              onChange={(e) => setAno(e.target.value)}
            >
              <option value="6º Ano">6º Ano</option>
              <option value="7º Ano">7º Ano</option>
              <option value="8º Ano">8º Ano</option>
              <option value="9º Ano">9º Ano</option>
              <option value="1º Ano EM">1º Ano EM</option>
            </select>
          </div>

          <div className="mb-3">
            <label className="form-label fw-semibold">Tema da Aula</label>
            <input
              type="text"
              className="form-control"
              placeholder="Ex: Frações no cotidiano"
              value={tema}
              onChange={(e) => setTema(e.target.value)}
            />
          </div>

          {erroIa && (
            <div className="alert alert-danger" role="alert">
              {erroIa}
            </div>
          )}

          <button
            type="button"
            onClick={handlePreencherComIa}
            className="btn btn-outline-primary w-100 mb-3"
            disabled={carregandoIa || carregando}
          >
            {carregandoIa ? (
              <>
                <span className="spinner-border spinner-border-sm me-2" />
                Gerando plano...
              </>
            ) : (
              '✨ Gerar plano com IA'
            )}
          </button>

          <hr />

          <div className="mb-3">
            <label className="form-label fw-semibold">Título da Aula *</label>
            <input
              type="text"
              className="form-control"
              placeholder="Ex: Frações no Cotidiano"
              value={titulo}
              onChange={(e) => setTitulo(e.target.value)}
            />
          </div>

          <div className="mb-3">
            <label className="form-label fw-semibold">Habilidade / Código BNCC *</label>
            <input
              type="text"
              className="form-control"
              placeholder="Ex: EF06MA07 - Compreender frações"
              value={habilidadeBncc}
              onChange={(e) => setHabilidadeBncc(e.target.value)}
            />
          </div>

          <div className="mb-3">
            <label className="form-label fw-semibold">Objetivo da Aula</label>
            <textarea
              className="form-control"
              rows={2}
              placeholder="O que o estudante aprenderá nesta aula?"
              value={objetivo}
              onChange={(e) => setObjetivo(e.target.value)}
            />
          </div>

          <div className="mb-3">
            <label className="form-label fw-semibold">Roteiro Metodológico</label>
            <textarea
              className="form-control"
              rows={3}
              placeholder="Passo a passo da aula (ex: 1. Acolhimento, 2. Prática, 3. Síntese)"
              value={metodologia}
              onChange={(e) => setMetodologia(e.target.value)}
            />
          </div>

          <button
            type="submit"
            className="btn btn-primary w-100 fw-semibold"
            disabled={carregando || carregandoIa}
          >
            {carregando ? 'Salvando plano...' : 'Salvar Plano de Aula'}
          </button>

        </form>
      </div>
    </div>
  );
}
