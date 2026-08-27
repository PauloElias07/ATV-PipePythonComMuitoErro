Pipeline CI com Python

Projeto desenvolvido para praticar Integração Contínua (CI) utilizando GitHub Actions e Python.

Pipeline

A pipeline é executada automaticamente a cada push na branch main e realiza as seguintes verificações:

Flake8 — análise estática e padronização do código.
Pytest — execução dos testes unitários.
Pytest-Cov — cobertura de código com mínimo de 90%.
Bandit — análise de segurança do código Python.
Gitleaks — detecção de chaves e credenciais expostas.
Objetivo

Simular um ambiente de CI capaz de identificar erros de código, falhas em testes, baixa cobertura e possíveis problemas de segurança antes que alterações sejam integradas ao projeto.
