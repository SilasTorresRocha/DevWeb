
'use client';

// Componente Filho: Listagem e exibição dos cartões de planos de aula
export default function ListaPlanos({
  planos,
  aoExcluirPlano,
  filtro,
  aoMudarFiltro,
  excluindoId
}) {
  // Filtra os planos de acordo com o filtro selecionado
  const planosFiltrados = planos.filter((plano) => {
    if (filtro === 'Todas') return true;
    return plano.disciplina === filtro;
  });

  return (
    <div>
      <div className="card shadow-sm mb-3">
        <div className="card-body py-2 d-flex justify-content-between align-items-center">
          <span className="text-muted small">
            Exibindo <strong>{planosFiltrados.length}</strong> de{' '}
            <strong>{planos.length}</strong> planos
          </span>

          <div className="d-flex align-items-center gap-2">
            <label className="form-label mb-0 small fw-semibold">
              Filtrar:
            </label>

            <select
              className="form-select form-select-sm w-auto"
              value={filtro}
              onChange={(e) => aoMudarFiltro(e.target.value)}
            >
              <option value="Todas">Todas as Disciplinas</option>
              <option value="Matemática">Matemática</option>
              <option value="Língua Portuguesa">Língua Portuguesa</option>
              <option value="Ciências">Ciências</option>
              <option value="História">História</option>
              <option value="Geografia">Geografia</option>
            </select>
          </div>
        </div>
      </div>

      {planosFiltrados.length === 0 ? (
        <div className="alert alert-warning text-center">
          Nenhum plano encontrado para este filtro.
        </div>
      ) : (
        planosFiltrados.map((plano) => {
          const excluindo = excluindoId === plano.id;

          return (
            <div key={plano.id} className="card shadow-sm mb-3">
              <div className="card-body">

                <div className="d-flex justify-content-between align-items-start mb-2">
                  <div>
                    <span className="badge bg-primary me-2">
                      {plano.disciplina}
                    </span>
                    <span className="badge bg-secondary">
                      {plano.ano}
                    </span>
                  </div>

                  <button
                    type="button"
                    onClick={() => aoExcluirPlano(plano.id)}
                    className="btn btn-sm btn-outline-danger"
                    title="Remover plano"
                    disabled={excluindo}
                  >
                    {excluindo ? (
                      <>
                        <span
                          className="spinner-border spinner-border-sm me-1"
                          role="status"
                          aria-hidden="true"
                        />
                        Excluindo...
                      </>
                    ) : (
                      'Excluir'
                    )}
                  </button>
                </div>

                <h5 className="card-title fw-bold text-dark mb-1">
                  {plano.titulo}
                </h5>

                <p className="card-subtitle mb-2 text-primary small font-monospace">
                  <strong>BNCC:</strong> {plano.habilidadeBncc}
                </p>

                <p className="card-text small text-secondary mb-1">
                  <strong>Objetivo:</strong> {plano.objetivo}
                </p>

                <p className="card-text small text-muted">
                  <strong>Metodologia:</strong> {plano.metodologia}
                </p>

              </div>
            </div>
          );
        })
      )}
    </div>
  );
}
