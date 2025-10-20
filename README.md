# PizzariaBot: Chatbot de Alto Desempenho para Atendimento de Pizzaria 🍕🤖

## 1. Visão Geral do Projeto

Este projeto demonstra um chatbot de atendimento ao cliente projetado para a automação e aceleração da tomada de pedidos em uma pizzaria. O principal diferencial é a utilização da plataforma Groq, garantindo respostas instantâneas, essenciais para uma excelente experiência do cliente no setor de alimentos.


### Objetivos Principais

* Automatizar mas consultas sobre o menu e pedidos diretos.
* Garantir uma velocidade de resposta inferior a 1 segundo, utilizando a inferência LPU da Groq.
* Manter a precisão nos dados de menu e preços através do Contexto do Sistema (\textit{System Prompt}).

## 2. Stack Tecnológica e Arquitetura

O \texttt{PizzariaBot} é construído sobre uma arquitetura robusta e focada em performance:

* **Interface (UI):** Chainlit
* **Orquestração/Lógica:** Python
* **Modelo de Linguagem (LLM):** Groq API (Modelo llama-3.3-70b-versatile)
* **Gestão de Segredos:** \texttt{python-dotenv}

## 3. Guia de Instalação e Execução

Siga os passos abaixo para configurar e iniciar o chatbot em seu ambiente local.

### 3.1. Pré-requisitos

Certifique-se de ter instalado:

* Python (Versão 3.10 ou superior recomendada)
* Uma conta Groq e sua \textbf{GROQ\_API\_KEY}.
* Git (para clonagem do repositório)

### 3.2. Setup do Ambiente

1.  **Clonar o Repositório:**
    ```bash
    git clone [LINK DO REPOSITÓRIO AQUI]
    cd [NOME DA PASTA DO PROJETO]
    ```

2.  **Criar e Ativar o Ambiente Virtual (\texttt{venv}):**
    ```bash
    python -m venv venv
    # Para Windows (PowerShell):
    .\venv\Scripts\Activate.ps1
    # Para Linux/macOS:
    source venv/bin/activate
    ```

3.  **Instalar Dependências:**
    ```bash
    pip install chainlit
    pip install groq
    pip install chainlit groq python-dotenv
    ```

### 3.3. Configuração de Variáveis de Ambiente

Para a segurança de sua chave de API, o projeto utiliza um arquivo \texttt{.env} que é ignorado pelo Git.

1.  **Criar o Arquivo \texttt{.env}:** Copie o conteúdo do arquivo \texttt{.env.example} e crie um novo arquivo chamado exatamente \texttt{.env} na raiz do projeto.

2.  **Inserir a Chave:** Edite o arquivo \texttt{.env} e insira sua chave de API da Groq:
    ```
    GROQ_API_KEY=CHAVE_AQUI
    ```

### 3.4. Execução do Chatbot

Execute o seguinte comando na raiz do projeto, com o ambiente virtual ativado:

```bash
chainlit run PizzariaBot.py -w