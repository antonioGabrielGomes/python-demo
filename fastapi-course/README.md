# Parte 1

## Configurando o Ambiente de Desenvolvimento
1. install python:  version python: 3.11

## Gerenciamento de Dependências com Poetry
2. install poetry: pipx install poetry: 1.7.1

## Criação do Projeto FastAPI e Instalação das Dependências
3. criar aplicação com poetry: poetry new fast_zero
4. poetry install  
5. poetry add fastapi uvicorn
6. poetry shell

## Primeira Execução de um "Hello, World!"
7. touch fast_zero/app.py
8. adicionar codigo inicial:
```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get('/')
    def read_root():
        return {'message': 'Olá Mundo!'}
```
9. uvicorn fast_zero.app:app

## Instalando as ferramentas de desenvolvimento
* taskipy: ferramenta para automatizar alguns comandos e simplificar o fluxo
* ruff: um linter, para dizer se não estamos fazendo nada esquisito no código
* blue: um formatador de código bastante amigável
* isort: uma ferramenta para ordenar os imports em ordem alfabética
* pytest: ferramenta para escrever e executar testes

10. poetry add --group dev pytest pytest-cov taskipy blue ruff httpx isort

## Configurando as ferramentas de desenvolvimento
* obs.: ver arquivo pyproject.toml
* obs2.: Para executar um comando, é bem mais simples, precisando somente passar a palavra task <comando>.
* Os comandos definidos fazem o seguinte:
    * lint: executa o ruff para ver se não temos nenhum problema com o código e checa se estamos conforme a PEP-8
    * format: formata o código usando blue e isort
    * run: executa o servidor de desenvolvimento do FastAPI
    * pre_test: executa a camada de lint antes de executar os teste
    * test: executa os testes com pytest de forma verbosa (-vv) e adiciona nosso código como base de cobertura
    * post_test: gera um report de cobertura após os testes

## Os efeitos dessas configurações de desenvolvimento
1. task lint
2. task format
3. task test

## Escrevendo o teste
* AAA


# Parte 2 

## Pydantic e a validação de dados
* Para que o Pydantic suporte a validação de emails, é necessário instalar o pydantic[email]
1. poetry add "pydantic[email]"

## Implementação do CRUD
* no código. :>

# Parte 3

## Configurando o Banco de Dados e Gerenciando Migrações com Alembic
* SQLAlchemy: ORM para sql
* pydantic-settings: gerenciar as configurações do app

## Configurações de ambiente e os 12 fatores
1. poetry add sqlalchemy
2. poetry add pydantic-settings

## Configurações do banco de dados:
1. criar um arquivo de models: touch fast_zero/models.py
2. fazer teste das tabelas: em tests/conftest.py, função def session()
3. criar arquivo para testar tabela: em tests/test_db.py
4. task test

## Configurar ambiente do banco
1. arquivo de configurações: touch fast_zero/settings.py
2. criar .env: DATABASE_URL="sqlite:///database.db"

## Instalando o Alembic e Criando a Primeira Migração
1. instalação: poetry add alembic
2. iniciar alembic: alembic init migrations
3. alterações para o migrations/env.py:
```
    # ...
    from alembic import context
    from fast_zero.settings import Settings
    from fast_zero.models import Base

    config = context.config
    config.set_main_option('sqlalchemy.url', Settings().DATABASE_URL)

    if config.config_file_name is not None:
        fileConfig(config.config_file_name)

    target_metadata = Base.metadata

    # ...
```

4. criar uma migração: alembic revision --autogenerate -m "create users table"
5. executa a migração:
    1. sqlite3 database.db
    2. .schema e .exit
6. alembic upgrade head