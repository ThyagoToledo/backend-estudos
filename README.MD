<div align="center">

# Backend Estudos

<p>Plano operacional de estudos continuos focado nos fundamentos de programacao BackEnd, persistencia relacional com SQLite e arquitetura de aplicacoes.</p>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  <img src="https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white" alt="PowerShell" />
  <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown" />
</p>

</div>

---

## Sobre o Repositorio

Este repositorio documenta e armazena os exercicios diarios, scripts de pratica e projetos elaborados a partir do cronograma de capacitacao tecnica para Programador BackEnd Junior.

O objetivo do primeiro ciclo de 30 dias consiste em dominar:
- Fundamentos solidos de logica e sintaxe em Python;
- Manipulacao de fluxos, funcoes, colecoes e arquivos locais (JSON);
- Modelagem e persistencia com banco relacional SQLite;
- Conceitos fundamentais do protocolo HTTP e arquitetura em camadas;
- Criacao de uma aplicacao CLI estruturada com testes automatizados e suite de aceitacao.

---

<details>
<summary><strong>Estrutura de Diretorios</strong></summary>

```text
backend-estudos/
|-- .gitignore                  # Arquivos e diretorios ignorados pelo Git
|-- README.MD                   # Documentacao principal do repositorio
|-- caderno-erros.md            # Registro formal de falhas tecnicas e aprendizados
|-- Docs/                       # Fichas teoricas e documentacao complementar
|   |-- api-futura.md
|   |-- ficha-http.md
|   `-- sql-tarefas.md
|-- semana-01/                  # Fundamentos de Python e exercicios da Semana 1
|   |-- d01_ambiente.py         # Dia 01: Cartao de visita, operacoes e formatacao
|   |-- d02_perfil.py           # Dia 02: Variaveis, input, tipos e media
|   `-- d07_calculadora_final.py
|-- semana-02/                  # Estruturas de dados, funcoes e POO
|-- semana-03/                  # Modelagem e consultas SQL (pratica.sql)
`-- projeto-tarefas/            # Projeto final do mes: CLI com SQLite e testes
    |-- README.md
    |-- banco.py
    |-- cli.py
    |-- servico.py
    |-- tarefa.py
    `-- tests/
```

</details>

<details>
<summary><strong>Como Executar Localmente</strong></summary>

### Pre-requisitos

- Python 3.10 ou superior instalado e configurado no PATH do sistema.
- Git configurado localmente.

### Clonagem e Execucao

1. Clone o repositorio:
   ```bash
   git clone https://github.com/ThyagoToledo/backend-estudos.git
   cd backend-estudos
   ```

2. Execucao dos scripts da Semana 01:
   ```bash
   # Executar o primeiro script de teste de ambiente
   py semana-01/d01_ambiente.py

   # Executar o script de perfil e calculo de media
   py semana-01/d02_perfil.py
   ```

</details>

<details>
<summary><strong>Cronograma Diario de Execucao</strong></summary>

- **Semana 01**: Fundamentos da linguagem, tipos, operadores, estruturas de controle e calculadora CLI.
- **Semana 02**: Listas, tuplas, conjuntos, dicionarios, tratamento de excecoes, persistencia em JSON e classes.
- **Semana 03**: Fundamentos de bancos relacionais, consultas SQL com SQLite, modulo sqlite3 e introducao a HTTP.
- **Semana 04**: Arquitetura em camadas, construcao do servico de tarefas, testes unitarios com unittest e criterios de aceitacao AT-01 a AT-15.

</details>

---

<div align="center">

### Autor

<a href="https://github.com/ThyagoToledo">
  <img src="https://github.com/ThyagoToledo.png" width="100px" style="border-radius: 8px; border: 2px solid #00E5FF; box-shadow: 0 0 10px #00E5FF;" alt="ThyagoToledo" />
</a>

<p>Desenvolvido exclusivamente por <strong><a href="https://github.com/ThyagoToledo">ThyagoToledo</a></strong>.</p>

</div>
