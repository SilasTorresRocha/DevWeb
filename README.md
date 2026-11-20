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

* [x] **API acessível por URL pública com documentação em `/docs`:** Swagger interativo completo.
* [x] **Código organizado em módulos:** Separação limpa entre rotas, esquemas, serviços e banco em memória.
* [x] **Modelos Pydantic alinhados ao Frontend:** Validação  dos dados de planos e requisições da IA.
* [x] **Códigos HTTP e mensagens adequadas:** `200 OK`, `201 Created`, `204 No Content` e `404 Not Found`.
* [x] **IA com papel real no fluxo docente:** Sugestão de habilidades BNCC e metodologia de aula a partir de tema e ano escolar.
* [x] **Credenciais protegidas fora do repositório:** Uso de `.env` com arquivo `.env.exemplo` de referência.

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

* [x] **API acessível por URL pública com documentação em `/docs`:** Swagger interativo completo.
* [x] **Código organizado em módulos:** Separação limpa entre rotas, esquemas, serviços e banco em memória.
* [x] **Modelos Pydantic alinhados ao Frontend:** Validação rigorosa dos dados de planos e requisições da IA.
* [x] **Códigos HTTP e mensagens adequadas:** `200 OK`, `201 Created`, `204 No Content` e `404 Not Found`.
* [x] **IA com papel real no fluxo docente:** Sugestão de habilidades BNCC e metodologia de aula a partir de tema e ano escolar.
* [x] **Credenciais protegidas fora do repositório:** Uso de `.env` com arquivo `.env.exemplo` de referência.

---


## Sprint 3 — Autenticação, Integração com API e Inteligência Artificial

**Período:** 16/11/2026 a 23/11/2026

### Backend

- [x] Implementar API com FastAPI.
- [x] Criar endpoint de cadastro de usuários.
- [x] Criar endpoint de login.
- [x] Implementar hash de senhas utilizando Argon2.
- [x] Implementar autenticação utilizando JWT.
- [x] Proteger endpoints de criação, listagem e exclusão de planos.
- [x] Proteger endpoint de geração de planos com inteligência artificial.
- [x] Garantir que usuários acessem somente seus próprios planos.
- [x] Implementar validação dos dados utilizando Pydantic.
- [x] Implementar integração com a API do Google Gemini.
- [x] Implementar tratamento de erros na integração com IA.
- [x] Implementar CORS configurável por variável de ambiente.
- [x] Configurar backend utilizando Docker.

### Frontend

- [x] Integrar frontend Next.js com a API FastAPI.
- [x] Implementar formulário de cadastro.
- [x] Implementar formulário de login.
- [x] Implementar autenticação e envio de token JWT nas requisições.
- [x] Implementar listagem de planos de aula do usuário autenticado.
- [x] Implementar criação de planos de aula.
- [x] Implementar exclusão de planos de aula.
- [x] Implementar filtros por disciplina.
- [x] Implementar geração de planos de aula utilizando IA.
- [x] Preencher automaticamente os campos do formulário com os dados gerados pela IA.
- [x] Implementar indicadores de carregamento durante operações.
- [x] Implementar mensagens de sucesso e erro.
- [x] Implementar tratamento de falhas de conexão com a API.
- [x] Configurar URL da API utilizando variável de ambiente.
- [x] Implementar botão para encerrar sessão.

### Segurança

- [x] Armazenar senhas utilizando hash, sem salvar senhas em texto puro.
- [x] Implementar autenticação baseada em JWT.
- [x] Exigir autenticação para operações protegidas.
- [x] Impedir que usuários excluam planos pertencentes a outros usuários.
- [ ] Implementar tratamento de sessão expirada no frontend.
- [ ] Revisar configurações de segurança para o ambiente de produção.

### Infraestrutura e configuração

- [x] Configurar Docker para o backend.
- [x] Configurar variáveis de ambiente para URL da API.
- [x] Configurar variáveis de ambiente para CORS.
- [x] Configurar arquivo `.env` para credenciais e configurações sensíveis.
- [x] Implementar configuração para execução local.
- [ ] Hospedar frontend em ambiente público.
- [ ] Hospedar backend em ambiente público.
- [ ] Configurar comunicação entre frontend e backend hospedados.
- [ ] Validar aplicação em ambiente de produção.

### Testes

- [x] Testar cadastro de usuário.
- [x] Testar login com credenciais válidas.
- [x] Testar login com credenciais inválidas.
- [x] Testar cadastro com e-mail já existente.
- [x] Testar acesso a endpoints protegidos sem autenticação.
- [x] Testar listagem de planos autenticada.
- [x] Testar criação de planos.
- [x] Testar exclusão de planos.
- [x] Testar geração de planos utilizando IA.
- [x] Testar indicadores de carregamento.
- [x] Testar mensagens de erro no frontend.
- [ ] Testar aplicação completa em ambiente hospedado.

### Observações

- A persistência dos dados ainda é realizada em memória.
- Os dados são perdidos quando o backend é reiniciado.
- A implementação da persistência utilizando banco de dados SQLModel está prevista para a Sprint 4.