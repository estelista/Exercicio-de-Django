# django-bsi4

API REST de produtos construída com Django e Django REST Framework, com CRUD completo, validações, filtros, ordenação, busca textual e paginação.

## Tecnologias

- Python 3.10+
- Django
- Django REST Framework
- drf-spectacular (documentação OpenAPI/Swagger)
- django-filter (filtros)
- SQLite

## Estrutura do projeto

```
django-bsi4/
├── manage.py
├── pyproject.toml
├── produtos.json              # dados de exemplo (fixture)
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── produtos/
    ├── models.py               # modelo Produto
    ├── admin.py                # configuração do Django Admin
    ├── serializers.py          # serialização e validações
    ├── filters.py               # filtros da API
    ├── views.py                 # ViewSet com filtros, ordenação e busca
    ├── pagination.py             # paginação customizada
    ├── tests.py                   # testes automatizados
    └── migrations/                # histórico do banco de dados
```

## Modelo de dados

`Produto`: `id`, `nome`, `preco`, `marca`, `estoque`, `descricao`

## Como rodar

### Pré-requisitos

- Python 3.10 ou superior
- [uv](https://docs.astral.sh/uv/) (gerenciador de pacotes e ambientes)

### Instalação

```bash
git clone <url-do-repositorio>
cd django-bsi4
uv sync
```

### Configurar o banco de dados

```bash
uv run python manage.py migrate
uv run python manage.py loaddata produtos.json
```

### Criar um usuário administrador

```bash
uv run python manage.py createsuperuser
```

### Rodar o servidor

```bash
uv run python manage.py runserver
```

A aplicação estará disponível em:

- API: http://127.0.0.1:8000/api/produtos/
- Documentação (Swagger): http://127.0.0.1:8000/api/docs/
- Painel administrativo: http://127.0.0.1:8000/admin/

## Rodando os testes

```bash
uv run python manage.py test
```

## Endpoints principais

| Método | URL                      | Descrição                    |
| ------ | ------------------------ | ----------------------------- |
| GET    | `/api/produtos/`         | Lista produtos (com filtros, ordenação, busca e paginação) |
| GET    | `/api/produtos/{id}/`    | Detalha um produto            |
| POST   | `/api/produtos/`         | Cria um novo produto          |
| PUT    | `/api/produtos/{id}/`    | Atualiza um produto            |
| DELETE | `/api/produtos/{id}/`    | Remove um produto              |

### Parâmetros de consulta suportados

- `preco_minimo`, `preco_maximo` — filtro por faixa de preço
- `marca` — filtro exato por marca
- `estoque_minimo`, `estoque_maximo` — filtro por faixa de estoque
- `search` — busca textual (nome, marca e descrição)
- `ordering` — ordenação (`nome`, `preco`, `marca`, `estoque`, `descricao`, com prefixo `-` para decrescente)
- `page`, `page_size` — paginação
