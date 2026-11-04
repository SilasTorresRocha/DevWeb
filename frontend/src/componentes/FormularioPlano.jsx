'use client';

import { useState } from 'react';

// Componente Filho: Formulário de cadastro de plano de aula
export default function FormularioPlano({ aoAdicionarPlano }) {
  // Estados locais para controlar os campos do formulário
  const [titulo, setTitulo] = useState('');
  const [disciplina, setDisciplina] = useState('Matemática');
  const [ano, setAno] = useState('6º Ano');
  const [habilidadeBncc, setHabilidadeBncc] = useState('');
  const [objetivo, setObjetivo] = useState('');
  const [metodologia, setMetodologia] = useState('');

  // Função para simular o papel da IA (preenchimento automático inteligente)
  function handlePreencherComIa() {
    setTitulo('Geometria Prática: Sólidos com Materiais Reciclados');
    setDisciplina('Matemática');
    setAno('6º Ano');
    setHabilidadeBncc('EF06MA17 - Identificar figuras espaciais e suas planificações.');
    setObjetivo('Reconhecer as propriedades dos prismas e pirâmides no cotidiano.');
    setMetodologia('1. Manipulação de caixas de papelão vazias (15 min). 2. Planificação manual no caderno (25 min). 3. Síntese coletiva (10 min).');
  }

  // Função disparada ao enviar o formulário
  function handleSubmit(evento) {
    evento.preventDefault();

    // Validação básica
    if (!titulo.trim() || !habilidadeBncc.trim()) {
      alert('Por favor, preencha pelo menos o Título e a Habilidade BNCC.');
      return;
    }

    const novoPlano = {
      id: Date.now(),
      titulo,
      disciplina,
      ano,
      habilidadeBncc,
      objetivo: objetivo || 'Objetivo a ser definido pelo professor.',
      metodologia: metodologia || 'Metodologia padrão da aula.'
    };

    // Comunica com o componente pai (Fluxo de dados inverso via props)
    aoAdicionarPlano(novoPlano);

    // Limpa os campos
    setTitulo('');
    setHabilidadeBncc('');
    setObjetivo('');
    setMetodologia('');
  }

  return (
    <div className="card shadow-sm mb-4">
      <div className="card-header bg-white d-flex justify-content-between align-items-center">
        <h5 className="mb-0 fw-bold">Novo Plano de Aula</h5>
        {/* Botão de simulação da IA */}
        <button
          type="button"
          onClick={handlePreencherComIa}
          className="btn btn-sm btn-outline-primary"
        >
          ✨ Preencher com IA
        </button>
      </div>

      <div className="card-body">
        <form onSubmit={handleSubmit}>
          
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

          <div className="row mb-3">
            <div className="col-md-6">
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

            <div className="col-md-6">
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

          <button type="submit" className="btn btn-primary w-100 fw-semibold">
            Salvar Plano de Aula
          </button>

        </form>
      </div>
    </div>
  );
}
