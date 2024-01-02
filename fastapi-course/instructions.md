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