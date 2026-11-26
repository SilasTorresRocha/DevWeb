# PlanoFácil - Sistema Web de Apoio ao Planejamento Docente com IA

Projeto desenvolvido para a disciplina de **Desenvolvimento de Aplicações Web (DWCO8A)** da **UTFPR - Campus Apucarana**, ministrada pelo **Prof. Luiz Rodrigues**, integrando a proposta de extensão de IA para Apoio de Professores da Educação Básica.

> O **PlanoFácil** é uma aplicação web desenvolvida para apoiar professores da Educação Básica na elaboração ágil de planos de aula alinhados à Base Nacional Comum Curricular (BNCC). Diante da fragmentação de informações e da sobrecarga de tarefas administrativas e burocráticas no cotidiano escolar, a plataforma centraliza a criação, visualização e organização dos planejamentos didáticos em um único ambiente. O sistema tem como público-alvo professores do ensino fundamental e médio das redes públicas e privadas. O papel da Inteligência Artificial no fluxo do usuário será atuar como um copiloto pedagógico: a partir do tema da aula e do ano escolar informados pelo docente, a IA sugere automaticamente habilidades curriculares pertinentes, objetivos de aprendizagem e um roteiro estruturado de atividades para a duração da aula, reduzindo drasticamente o tempo gasto no trabalho braçal de planejamento.

---

## 🛠️ Stack Tecnológica

- **Frontend:** Next.js, React, Bootstrap 5
- **Backend:** Python 3.10+, FastAPI, Pydantic, HTTPX
- **Inteligência Artificial:** Google Gemini via REST, com cache e fallback
- **Autenticação:** JWT e hash de senhas com Argon2
- **Containerização:** Docker e Docker Compose
- **Hospedagem:** Vercel (frontend) e Render (backend)

---

## 🚀 Como Executar o Backend

### Opção 1: Com Docker (Recomendado)

Na raiz do projeto, execute:

```bash
docker-compose up -d --build backend
```

A API estará disponível em:

- Documentação Swagger Interativa: http://localhost:8000/docs
- Rota de Status: http://localhost:8000/

### Opção 2: Localmente com Python

1. Acesse a pasta do backend:

   ```bash
   cd backend
   ```
2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
3. Inicie o servidor:

   ```bash
   uvicorn main:app --reload --port 8000
   ```

---

## 📁 Estrutura do Projeto

A estrutura abaixo destaca os principais arquivos e módulos da aplicação, incluindo as alterações realizadas durante a Sprint 3.

```text
DevWeb/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env                  # Variáveis locais (não versionadas)
│   ├── .env.exemplo
│   ├── main.py               # Inicialização da API, CORS e Swagger
│   ├── banco_memoria.py      # Armazenamento em memória
│   ├── esquemas/
│   │   ├── plano.py          # Modelos Pydantic de planos
│   │   └── usuario.py        # Modelos Pydantic de usuários
│   ├── rotas/
│   │   ├── autenticacao.py   # Cadastro e login
│   │   ├── planos.py         # CRUD de planos
│   │   └── inteligencia.py    # Endpoint de geração por IA
│   ├── seguranca.py          # Hash de senha, JWT e autenticação
│   └── servicos/
│       └── servico_ia.py     # Integração com Gemini, cache e fallback
│
├── frontend/
│   ├── Dockerfile
│   ├── next.config.js
│   ├── package.json
│   └── src/
│       ├── app/
│       │   ├── globals.css   # Estilos globais
│       │   ├── layout.jsx    # Layout da aplicação
│       │   └── page.jsx      # Página principal e fluxo da aplicação
│       ├── componentes/
│       │   ├── FormularioLogin.jsx  # Cadastro/login
│       │   ├── FormularioPlano.jsx  # Formulário de planos
│       │   └── ListaPlanos.jsx      # Listagem e ações dos planos
│       └── dados/
│           └── planosIniciais.js    # Dados iniciais da versão Sprint 1
│
├── docker-compose.yml
└── README.md
```

> **Observação:** a árvore representa os principais arquivos conhecidos durante a documentação. Antes da entrega final, confira no repositório se algum arquivo foi criado, renomeado ou removido durante a Sprint 3, especialmente no frontend. O arquivo `planosIniciais.js` pertence à estrutura inicial; a aplicação da Sprint 3 deve utilizar os dados retornados pela API real.

---

## 🎯 Entregáveis e Critérios Atendidos (Sprint 2)

- [X] API acessível por URL pública com documentação em `/docs`.
- [X] Código organizado em módulos: rotas, esquemas, serviços e banco em memória.
- [X] Modelos Pydantic alinhados ao frontend.
- [X] Códigos HTTP e mensagens adequadas (`200 OK`, `201 Created`, `204 No Content` e `404 Not Found`).
- [X] IA integrada ao fluxo docente, sugerindo habilidades BNCC e metodologia a partir do tema e ano escolar.
- [X] Credenciais protegidas fora do repositório, com uso de `.env` e `.env.exemplo`.

---

## Sprint 3 — Hospedagem e Integração com API

**Período:** 16/11/2026 a 23/11/2026

**Foco:** aplicação web hospedada e integrada à API real, sem dados mockados.

### Configurações e escolhas importantes

- **Frontend:** hospedado na Vercel, com o diretório raiz configurado como `frontend`.
- **Backend:** hospedado no Render, utilizando Docker e o diretório `backend`.
- **URL da API:** configurada no frontend por meio da variável de ambiente `NEXT_PUBLIC_API_URL`.
- **CORS:** configurado no backend por meio da variável `FRONTEND_URL`, incluindo a URL pública da Vercel e as origens locais utilizadas no desenvolvimento.
- **Porta do backend:** o Dockerfile utiliza a variável `PORT` disponibilizada pela hospedagem, com `8000` como valor padrão.
- **Credenciais:** `GEMINI_API_KEY` e `SECRET_KEY` configuradas como variáveis de ambiente no Render, sem serem incluídas no repositório.

### Requisitos da Sprint

- [X] Site acessível por URL pública, consumindo a API real hospedada.
- [X] Login funcional, com token JWT enviado nas requisições protegidas.
- [X] JWT protegendo endpoints de escrita e dados sensíveis.
- [X] Estados de carregamento e de erro tratados na interface.
- [X] URL da API e CORS configurados por variáveis de ambiente.
- [X] Fluxo de geração de planos utilizando a funcionalidade de IA integrado e testado em ambiente hospedado.
- [X] Aplicação testada em produção, incluindo cadastro, login, criação, listagem, exclusão e geração de planos por IA.

### Hospedagem

- **Frontend (Vercel):** [https://dev-web-delta.vercel.app]
- **Backend (Render):** [https://planofacil-backend.onrender.com]
- **Documentação da API:** disponível na rota `/docs` do backend hospedado.

### Observação

A persistência dos dados ainda é realizada em memória. Os dados são perdidos quando o backend é reiniciado. A implementação de persistência utilizando banco de dados SQLModel está prevista para a Sprint 4.

## Sprint 4 — Banco de Dados e Manual do Usuário

**Período:** 24/11/2026 a 30/11/2026

**Foco:** implementação de persistência real utilizando SQLModel, conclusão do sistema em produção e elaboração do manual do usuário.

### Checklist de desenvolvimento

#### 1. Preparação do banco de dados

- [X] Escolher e configurar um banco de dados compatível com SQLModel (PostgreSQL recomendado para produção).
- [X] Criar uma instância de banco de dados hospedada (Neon, Supabase ou Render).
- [X] Obter a URL de conexão com o banco de dados.
- [X] Configurar a URL de conexão por meio de variável de ambiente.
- [X] Atualizar as dependências do backend para incluir SQLModel e o driver do banco escolhido.
- [ ] Configurar a conexão e o gerenciamento de sessões do banco de dados.

#### 2. Implementação dos modelos SQLModel

- [X] Identificar as entidades existentes no sistema e seus atributos.
- [X] Criar os modelos SQLModel correspondentes às entidades.
- [X] Definir corretamente os tipos dos atributos e as chaves primárias.
- [X] Definir os relacionamentos entre usuários e planos.
- [X] Configurar as chaves estrangeiras e os relacionamentos necessários.
- [X] Implementar a criação das tabelas no banco de dados.
- [ ] Verificar se os modelos estão coerentes com os schemas Pydantic utilizados pela API.

#### 3. Integração da API com o banco de dados

- [X] Substituir o armazenamento em memória pela persistência no banco de dados.
- [X] Adaptar o cadastro de usuários para salvar os registros no banco.
- [X] Adaptar o login para consultar os usuários armazenados no banco.
- [X] Manter a validação de senhas com Argon2 e a autenticação JWT.
- [X] Adaptar a criação de planos para persistir os dados no banco.
- [X] Adaptar a listagem de planos para consultar os registros do banco.
- [X] Adaptar a exclusão de planos para remover os registros correspondentes.
- [X] Garantir que cada usuário tenha acesso somente aos seus próprios planos.
- [X] Preservar os códigos HTTP e as mensagens de erro adequados.
- [ ] Garantir que a geração por IA continue integrada ao fluxo de criação de planos.

#### 4. Testes de persistência e integração

- [ ] Testar o cadastro de usuários.
- [ ] Testar o login e a autenticação após o cadastro.
- [ ] Testar a criação, listagem e exclusão de planos.
- [ ] Verificar o isolamento dos dados entre diferentes usuários.
- [ ] Reiniciar a API e verificar se os dados continuam disponíveis.
- [ ] Reiniciar o serviço de hospedagem e verificar a persistência dos registros.
- [ ] Testar novamente a geração de planos por IA.
- [ ] Verificar se os principais fluxos funcionam sem erros críticos.

#### 5. Atualização da hospedagem

- [ ] Configurar a variável de ambiente da conexão com o banco no Render.
- [ ] Garantir que a API hospedada utilize o banco de dados de produção.
- [ ] Atualizar o backend hospedado com as alterações da Sprint 4.
- [ ] Verificar os logs da aplicação e corrigir eventuais erros.
- [ ] Testar o sistema completo utilizando o frontend da Vercel e a API do Render.
- [ ] Confirmar que os dados permanecem salvos após reinicializações.

#### 6. Manual do usuário

- [ ] Elaborar um manual voltado ao usuário final, sem exigir conhecimentos técnicos.
- [ ] Apresentar o objetivo e as funcionalidades do PlanoFácil.
- [ ] Documentar o processo de cadastro e login.
- [ ] Explicar como criar um plano de aula.
- [ ] Explicar como utilizar a funcionalidade de geração por IA.
- [ ] Mostrar como visualizar e organizar os planos criados.
- [ ] Explicar como excluir um plano.
- [ ] Adicionar capturas de tela para facilitar a compreensão.
- [ ] Revisar a clareza das instruções e gerar o documento em PDF.

#### 7. Finalização e entrega

- [ ] Revisar o README e atualizar a estrutura do projeto.
- [ ] Atualizar as instruções de instalação e execução do frontend e backend.
- [ ] Conferir as variáveis de ambiente necessárias e o arquivo `.env.exemplo`.
- [ ] Verificar se não existem credenciais ou informações sensíveis no repositório.
- [ ] Conferir o histórico de commits no GitHub.
- [ ] Gerar a documentação do projeto em PDF.
- [ ] Finalizar o manual do usuário em PDF.
- [ ] Preparar o código em ZIP contendo as pastas `frontend/` e `backend/`.
- [ ] Conferir se o repositório Git está público e atualizado.
- [ ] Preparar o pitch de até 2 minutos, focado no usuário final.

### Critérios de conclusão da Sprint 4

- [ ] Modelos SQLModel coerentes com as entidades, incluindo tipos e relacionamentos corretos.
- [ ] Dados mantidos após reiniciar a API.
- [ ] Sistema hospedado utilizando banco de dados persistente.
- [ ] Fluxo principal funcionando sem erros críticos em produção.
- [ ] Manual do usuário claro e focado nos principais fluxos.
- [ ] Pitch de até 2 minutos preparado e demonstrando o sistema.

### Entrega Final — 30/11/2026

A entrega final será composta por três arquivos:

1. **Documentação (PDF):** definição da equipe, descrição do sistema e README do projeto.
2. **Manual do usuário (PDF):** guia de utilização voltado ao usuário final.
3. **Código (ZIP):** contendo as pastas `frontend/` e `backend/`.

O repositório Git deverá permanecer público, com o link informado na documentação.

**Resultado esperado:** PlanoFácil completamente funcional em produção, com autenticação, geração de planos por IA e persistência real em banco de dados, acompanhado de documentação técnica e manual de utilização.
