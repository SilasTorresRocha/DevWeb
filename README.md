# PlanoFácil - Sistema Web de Apoio ao Planejamento Docente com IA

Projeto desenvolvido para a disciplina de **Desenvolvimento de Aplicações Web (DWCO8A)** da **UTFPR - Campus Apucarana**, ministrada pelo **Prof. Luiz Rodrigues**, integrando a proposta de extensão de IA para Apoio de Professores da Educação Básica.

---

> O **PlanoFácil** é uma aplicação web desenvolvida para apoiar professores da Educação Básica na elaboração ágil de planos de aula alinhados à Base Nacional Comum Curricular (BNCC). Diante da fragmentação de informações e da sobrecarga de tarefas administrativas e burocráticas no cotidiano escolar, a plataforma centraliza a criação, visualização e organização dos planejamentos didáticos em um único ambiente. O sistema tem como público-alvo professores do ensino fundamental e médio das redes públicas e privadas. O papel da Inteligência Artificial no fluxo do usuário será atuar como um copiloto pedagógico: a partir do tema da aula e do ano escolar informados pelo docente, a IA sugere automaticamente habilidades curriculares pertinentes, objetivos de aprendizagem e um roteiro estruturado de atividades para a duração da aula, reduzindo drasticamente o tempo gasto no trabalho braçal de planejamento.

---

## 🛠️ Stack Tecnológica

* **Frontend (Sprint 1):** Next.js (apenas como frontend), React, Bootstrap 5
* **Backend (Sprint 2):** Python 3.10+, FastAPI, Pydantic, HTTPX
* **Inteligência Artificial:** Google Gemini (Gemini 1.5 Flash via REST) com Cache e Fallback
* **Containerização:** Docker & Docker Compose

---

## 🚀 Como Executar o Backend (Sprint 2)

### Opção 1: Com Docker (Recomendado)

Na raiz do projeto, execute:

```bash
docker-compose up -d --build backend
```

A API estará disponível em:

* Documentação Swagger Interativa: [http://localhost:8000/docs](http://localhost:8000/docs)
* Rota de Status: [http://localhost:8000/](http://localhost:8000/)

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

## 📁 Estrutura Modular do Backend

O backend foi estruturado em módulos independentes com nomenclatura em português, alinhado aos conceitos de APIs RESTful e FastAPI ensinados em aula:

```text
backend/
├── Dockerfile                   # Container Docker para execução isolada
├── requirements.txt             # Dependências da aplicação (FastAPI, Pydantic, HTTPX)
├── .env                         # Variáveis de ambiente e chave de API (ignorado pelo Git)
├── .env.exemplo                 # Exemplo de configuração para o repositório
├── main.py                      # Ponto de entrada FastAPI com CORS e Swagger em /docs
├── banco_memoria.py             # Dados em memória para a Sprint 2 (conforme especificação)
├── esquemas/
│   └── plano.py                 # Modelos Pydantic de validação (entradas e saídas)
├── rotas/
│   ├── planos.py                # Endpoints CRUD dos planos de aula (/api/planos)
│   └── inteligencia.py          # Endpoint de geração com IA (/api/ia/gerar-plano)
└── servicos/
    └── servico_ia.py            # Integração com Gemini, cache e plano de contingência anti-falha
```

---

## 🎯 Entregáveis e Critérios Atendidos (Sprint 2)

* [X] **API acessível por URL pública com documentação em `/docs`:** Swagger interativo completo.
* [X] **Código organizado em módulos:** Separação limpa entre rotas, esquemas, serviços e banco em memória.
* [X] **Modelos Pydantic alinhados ao Frontend:** Validação  dos dados de planos e requisições da IA.
* [X] **Códigos HTTP e mensagens adequadas:** `200 OK`, `201 Created`, `204 No Content` e `404 Not Found`.
* [X] **IA com papel real no fluxo docente:** Sugestão de habilidades BNCC e metodologia de aula a partir de tema e ano escolar.
* [X] **Credenciais protegidas fora do repositório:** Uso de `.env` com arquivo `.env.exemplo` de referência.

---

## 🚀 Como Executar o Backend (Sprint 2)

### Opção 1: Com Docker (Recomendado)

Na raiz do projeto, execute:

```bash
docker-compose up -d --build backend
```

A API estará disponível em:

* Documentação Swagger Interativa: [http://localhost:8000/docs](http://localhost:8000/docs)
* Rota de Status: [http://localhost:8000/](http://localhost:8000/)

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

## 📁 Estrutura Modular do Backend

O backend foi estruturado em módulos independentes com nomenclatura em português, alinhado aos conceitos de APIs RESTful e FastAPI ensinados em aula:

```text
backend/
├── Dockerfile                   # Container Docker para execução isolada
├── requirements.txt             # Dependências da aplicação (FastAPI, Pydantic, HTTPX)
├── .env                         # Variáveis de ambiente e chave de API (ignorado pelo Git)
├── .env.exemplo                 # Exemplo de configuração para o repositório
├── main.py                      # Ponto de entrada FastAPI com CORS e Swagger em /docs
├── banco_memoria.py             # Dados em memória para a Sprint 2 (conforme especificação)
├── esquemas/
│   └── plano.py                 # Modelos Pydantic de validação (entradas e saídas)
├── rotas/
│   ├── planos.py                # Endpoints CRUD dos planos de aula (/api/planos)
│   └── inteligencia.py          # Endpoint de geração com IA (/api/ia/gerar-plano)
└── servicos/
    └── servico_ia.py            # Integração com Gemini, cache e plano de contingência anti-falha
```

---

## 🎯 Entregáveis e Critérios Atendidos (Sprint 2)

* [X] **API acessível por URL pública com documentação em `/docs`:** Swagger interativo completo.
* [X] **Código organizado em módulos:** Separação limpa entre rotas, esquemas, serviços e banco em memória.
* [X] **Modelos Pydantic alinhados ao Frontend:** Validação rigorosa dos dados de planos e requisições da IA.
* [X] **Códigos HTTP e mensagens adequadas:** `200 OK`, `201 Created`, `204 No Content` e `404 Not Found`.
* [X] **IA com papel real no fluxo docente:** Sugestão de habilidades BNCC e metodologia de aula a partir de tema e ano escolar.
* [X] **Credenciais protegidas fora do repositório:** Uso de `.env` com arquivo `.env.exemplo` de referência.

---

## Sprint 3 — Autenticação, Integração com API e Inteligência Artificial

**Período:** 16/11/2026 a 23/11/2026

### Backend

- [X] Implementar API com FastAPI.
- [X] Criar endpoint de cadastro de usuários.
- [X] Criar endpoint de login.
- [X] Implementar hash de senhas utilizando Argon2.
- [X] Implementar autenticação utilizando JWT.
- [X] Proteger endpoints de criação, listagem e exclusão de planos.
- [X] Proteger endpoint de geração de planos com inteligência artificial.
- [X] Garantir que usuários acessem somente seus próprios planos.
- [X] Implementar validação dos dados utilizando Pydantic.
- [X] Implementar integração com a API do Google Gemini.
- [X] Implementar tratamento de erros na integração com IA.
- [X] Implementar CORS configurável por variável de ambiente.
- [X] Configurar backend utilizando Docker.

### Frontend

- [X] Integrar frontend Next.js com a API FastAPI.
- [X] Implementar formulário de cadastro.
- [X] Implementar formulário de login.
- [X] Implementar autenticação e envio de token JWT nas requisições.
- [X] Implementar listagem de planos de aula do usuário autenticado.
- [X] Implementar criação de planos de aula.
- [X] Implementar exclusão de planos de aula.
- [X] Implementar filtros por disciplina.
- [X] Implementar geração de planos de aula utilizando IA.
- [X] Preencher automaticamente os campos do formulário com os dados gerados pela IA.
- [X] Implementar indicadores de carregamento durante operações.
- [X] Implementar mensagens de sucesso e erro.
- [X] Implementar tratamento de falhas de conexão com a API.
- [X] Configurar URL da API utilizando variável de ambiente.
- [X] Implementar botão para encerrar sessão.

### Segurança

- [X] Armazenar senhas utilizando hash, sem salvar senhas em texto puro.
- [X] Implementar autenticação baseada em JWT.
- [X] Exigir autenticação para operações protegidas.
- [X] Impedir que usuários excluam planos pertencentes a outros usuários.
- [X] Implementar tratamento de sessão expirada no frontend.
- [ ] Revisar configurações de segurança para o ambiente de produção.

### Infraestrutura e configuração

- [X] Configurar Docker para o backend.
- [X] Configurar variáveis de ambiente para URL da API.
- [X] Configurar variáveis de ambiente para CORS.
- [X] Configurar arquivo `.env` para credenciais e configurações sensíveis.
- [X] Implementar configuração para execução local.
- [ ] Hospedar frontend em ambiente público.
- [ ] Hospedar backend em ambiente público.
- [ ] Configurar comunicação entre frontend e backend hospedados.
- [ ] Validar aplicação em ambiente de produção.

### Testes

- [X] Testar cadastro de usuário.
- [X] Testar login com credenciais válidas.
- [X] Testar login com credenciais inválidas.
- [X] Testar cadastro com e-mail já existente.
- [X] Testar acesso a endpoints protegidos sem autenticação.
- [X] Testar listagem de planos autenticada.
- [X] Testar criação de planos.
- [X] Testar exclusão de planos.
- [X] Testar geração de planos utilizando IA.
- [X] Testar indicadores de carregamento.
- [X] Testar mensagens de erro no frontend.
- [ ] Testar aplicação completa em ambiente hospedado.

### Observações

- A persistência dos dados ainda é realizada em memória.
- Os dados são perdidos quando o backend é reiniciado.
- A implementação da persistência utilizando banco de dados SQLModel está prevista para a Sprint 4.
