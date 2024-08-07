# FastAPI ProjectSnippet

Este projeto serve como um template para criar uma nova API utilizando o FastAPI. Ele inclui módulos para autenticação por bearer token, conexão com base de dados usando SQLAlchemy e um middleware para centralizar as requisições. Tudo isso desenvolvido em Python.

## Sumário

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Funcionalidades](#funcionalidades)
  - [Autenticação](#autenticação)
  - [Base de Dados](#base-de-dados)
  - [Middleware](#middleware)
- [Licença](#licença)

## Instalação
Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/fastapi-projectsnippet.git
cd fastapi-projectsnippet
pip install -r requirements.txt
```

## Configuração
Ajuste o arquivo `.env.sample` com os seus dados.


## Funcionalidades
  #### Autenticação
  O módulo de autenticação utiliza JWT tokens do tipo Bearer para proteger as rotas da API. A validação foi colocada como injeção de dependência no arquivo app/routes/my_route.py.

  #### Base de Dados
  A conexão com a base de dados é gerenciada pelo SQLAlchemy, no arquivo app/config/database.py.

  #### Middleware
  O middleware centraliza as requisições, permitindo a inclusão de validações, tratamento de erros e outras operações comuns a todas as requisições antes ou depois da execução.

## Licença
Este projeto está licenciado sob os termos da licença MIT.
