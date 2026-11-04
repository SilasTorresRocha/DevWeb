'use client';

import { useState } from 'react';
import FormularioPlano from '../componentes/FormularioPlano';
import ListaPlanos from '../componentes/ListaPlanos';
import { planosIniciais } from '../dados/planosIniciais';

// Componente Pai Principal (mantém o Estado da UI)
export default function PaginaPrincipal() {
  // Estado que armazena a lista de planos de aula
  const [planos, setPlanos] = useState(planosIniciais);

  // Estado que armazena o filtro de disciplina
  const [filtro, setFiltro] = useState('Todas');

  // Estado para feedback visual simples
  const [mensagemSucesso, setMensagemSucesso] = useState('');

  // Função que adiciona um novo plano (passada via props para o FormularioPlano)
  function handleAdicionarPlano(novoPlano) {
    // Atualiza o estado adicionando o novo plano no início da lista
    setPlanos([novoPlano, ...planos]);
    
    // Dispara o feedback visual
    setMensagemSucesso('Plano de aula adicionado com sucesso!');
    setTimeout(() => setMensagemSucesso(''), 4000);
  }

  // Função que remove um plano (passada via props para o ListaPlanos)
  function handleExcluirPlano(idParaRemover) {
    setPlanos(planos.filter((plano) => plano.id !== idParaRemover));
    setMensagemSucesso('Plano removido com sucesso!');
    setTimeout(() => setMensagemSucesso(''), 4000);
  }

  return (
    <div>
      {/* Barra de Navegação Simples (Bootstrap) */}
      <nav className="navbar navbar-dark bg-primary shadow-sm mb-4">
        <div className="container">
          <span className="navbar-brand fw-bold fs-4">
            PlanoFácil
          </span>
          <span className="navbar-text text-white small">
            Apoio ao Planejamento Docente com IA
          </span>
        </div>
      </nav>

      {/* Conteúdo da Página */}
      <div className="container pb-5">
        
        {/* Feedback Visual (Alert do Bootstrap) */}
        {mensagemSucesso && (
          <div className="alert alert-success alert-dismissible fade show" role="alert">
            {mensagemSucesso}
            <button
              type="button"
              className="btn-close"
              onClick={() => setMensagemSucesso('')}
              aria-label="Fechar"
            ></button>
          </div>
        )}

        {/* Grid com 2 colunas: Formulário à esquerda e Lista à direita */}
        <div className="row">
          
          {/* Coluna 1: Formulário (Componente Filho) */}
          <div className="col-lg-5">
            <FormularioPlano aoAdicionarPlano={handleAdicionarPlano} />
          </div>

          {/* Coluna 2: Listagem (Componente Filho) */}
          <div className="col-lg-7">
            <ListaPlanos
              planos={planos}
              aoExcluirPlano={handleExcluirPlano}
              filtro={filtro}
              aoMudarFiltro={setFiltro}
            />
          </div>

        </div>
      </div>
    </div>
  );
}
