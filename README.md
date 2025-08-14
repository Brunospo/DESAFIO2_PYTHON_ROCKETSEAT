# 🥗 API de Refeições com Flask + Docker

Este projeto é uma API RESTful construída com **Flask** que permite o gerenciamento de **usuários** e **refeições**. Usuários podem se registrar, autenticar e, uma vez logados, cadastrar e gerenciar suas refeições.

A aplicação está conteinerizada com **Docker Compose** para facilitar o desenvolvimento e o deploy.

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Docker
- Docker Compose
- PostgreSQL

## 📦 Como rodar o projeto com Docker Compose

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Passos

1. Clone este repositório:

```bash
git clone https://github.com/Brunospo/DESAFIO2_PYTHON_ROCKETSEAT.git
cd DESAFIO2_PYTHON_ROCKETSEAT
```

2. Copie o arquivo .env.example para um novo arquivo chamado .env e preencha com as suas configurações:

```bash
cp .env.example .env
```

3. Preencha as variáveis no ``.env``.

4. Construa e suba os containers:

```bash
docker-compose up --build
```

5. A API estará disponível em: <http://localhost:5000>

## 🔐 Autenticação

A autenticação utiliza **Flask-Login**, com sessões. O login é feito via POST para ``/login``, e o token de sessão é gerenciado automaticamente pelo servidor (cookies). Rotas protegidas utilizam ``@login_required``.

## 🧪 Endpoints da API

### 📁 Usuários

| Método | Rota              | Descrição                     | Protegida |
| ------ | ----------------- | ----------------------------- | --------- |
| POST   | `/user`           | Criar novo usuário            | ❌         |
| POST   | `/login`          | Fazer login                   | ❌         |
| GET    | `/logout`         | Fazer logout                  | ✅         |
| GET    | `/user/<user_id>` | Buscar informações do usuário | ✅         |
| PATCH  | `/user/<user_id>` | Atualizar dados do usuário    | ✅         |
| DELETE | `/user/<user_id>` | Deletar usuário               | ✅         |

### 🍽️ Refeições

| Método | Rota                     | Descrição                            | Protegida |
| ------ | ------------------------ | ------------------------------------ | --------- |
| POST   | `/meal/register`         | Cadastrar nova refeição              | ✅         |
| GET    | `/meal/list`             | Listar todas as refeições do usuário | ✅         |
| GET    | `/meal/<meal_id>`        | Obter detalhes de uma refeição       | ✅         |
| PUT    | `/meal/update/<meal_id>` | Atualizar uma refeição               | ✅         |
| DELETE | `/meal/delete/<meal_id>` | Deletar uma refeição                 | ✅         |

## 📂 Estrutura do Projeto

```markdown
DESAFIO2_PYTHON_ROCKETSEAT/
│
├── app/
│   ├── __init__.py
│   ├── meal_controller.py
│   ├── routes.py
│   └── user_controller.py
│
├── models/
│   ├── __init__.py
│   ├── meal.py
│   └── user.py
│
├── .dockerignore
├── .env.example
├── api.py
├── docker-compose.yaml
├── Dockerfile
├── README.md
└── requirements.txt

```

## 📝 Arquivo .env.example

Este é o formato do arquivo .env.example que você deve copiar para .env e preencher com as suas credenciais.

```bash
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=seu_banco
SECRET_KEY=sua_chave_secreta
DATABASE_URL=postgresql://seu_usuario:sua_senha@db:5432/seu_banco

FLASK_APP=app:create_app
```

### Explicação das variáveis

- POSTGRES_USER: Nome do usuário do banco de dados PostgreSQL.

- POSTGRES_PASSWORD: Senha do usuário do banco de dados.

- POSTGRES_DB: Nome do banco de dados PostgreSQL.

- SECRET_KEY: Chave secreta utilizada pelo Flask (para sessões, segurança, etc.).

- DATABASE_URL: URL completa para conexão com o banco de dados PostgreSQL.

- FLASK_APP: O caminho para a função create_app que inicializa a aplicação Flask.

## 🧠 Observações

- As rotas protegidas só funcionam com usuários autenticados.

- Para testar facilmente via Insomnia ou Postman, use uma coleção que respeite cookies ou implemente token-based auth no futuro.

- A estrutura está preparada para crescimento modular: controllers, models e rotas estão separados.

- Considere implementar JWT para tornar a API stateless, se for utilizada por front-ends independentes (ex: mobile apps ou SPAs).
