# 🎤 Agente Cantor

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Agno](https://img.shields.io/badge/Framework-Agno-6E56CF)
![OpenAI](https://img.shields.io/badge/Modelo-GPT--4o--mini-10A37F?logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-Ativo-brightgreen)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-A%20definir-lightgrey)

Um agente de IA conversacional que assume a persona de um **cantor**, construído com a framework [Agno](https://github.com/agno-agi/agno) e o modelo **GPT-4o-mini** da OpenAI. O agente roda diretamente no terminal, permitindo uma conversa contínua de perguntas e respostas até que o usuário decida encerrar a sessão.

---

## 📋 Sumário

- [Sobre o projeto](#-sobre-o-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Como usar](#-como-usar)
- [Estrutura do código](#-estrutura-do-código)
- [Exemplos de uso](#-exemplos-de-uso)
- [Solução de problemas comuns](#-solução-de-problemas-comuns)
- [Autor](#-autor)
- [Licença](#-licença)

---

## 📖 Sobre o projeto

Este projeto implementa um **agente de IA com personalidade de cantor**, capaz de responder perguntas, criar letras, dar opiniões musicais e conversar de forma criativa e descontraída. O agente utiliza a framework **Agno** para orquestrar a comunicação com o modelo **GPT-4o-mini** da OpenAI, formatando as respostas em markdown.

A interação acontece via **terminal**, em um loop contínuo: o usuário digita uma pergunta, o agente responde, e o ciclo se repete até que o usuário digite um dos comandos de saída.

---

## ✅ Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- **Python 3.10 ou superior**
- **pip** (gerenciador de pacotes do Python)
- Uma **chave de API da OpenAI** válida ([obtenha aqui](https://platform.openai.com/api-keys))
- Conexão com a internet (necessária para chamadas à API da OpenAI)

### Dependências principais

| Pacote          | Finalidade                                      |
|-----------------|--------------------------------------------------|
| `agno`          | Framework para criação e orquestração do agente  |
| `openai`        | Integração com os modelos da OpenAI              |
| `python-dotenv` | Carregamento de variáveis de ambiente (.env)     |

---

## ⚙️ Instalação

Siga os passos abaixo para configurar o projeto em sua máquina local.

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
```

Ative o ambiente virtual:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install agno openai python-dotenv
```

> 💡 Se o projeto possuir um arquivo `requirements.txt`, você pode instalar tudo de uma vez com:
> ```bash
> pip install -r requirements.txt
> ```

---

## 🔐 Configuração

O projeto utiliza variáveis de ambiente para armazenar a chave de API da OpenAI de forma segura, sem expor credenciais diretamente no código.

### 1. Crie o arquivo `.env`

Na raiz do projeto, crie um arquivo chamado `.env`:

```bash
touch .env
```

### 2. Adicione sua chave da OpenAI

Abra o arquivo `.env` e insira o seguinte conteúdo:

```env
OPENAI_API_KEY=sua_chave_aqui
```

> ⚠️ **Importante:** nunca compartilhe sua chave de API publicamente ou faça commit do arquivo `.env` no repositório. Adicione-o ao `.gitignore`:

```gitignore
.env
```

### 3. Verifique se a chave está sendo carregada

O código utiliza a biblioteca `python-dotenv` para carregar automaticamente as variáveis do arquivo `.env` no início da execução.

---

## 🚀 Como usar

Após instalar as dependências e configurar o `.env`, execute o agente com:

```bash
python main.py
```

> Substitua `main.py` pelo nome real do arquivo principal do seu projeto, caso seja diferente.

### Fluxo de interação

1. O terminal exibirá a mensagem `Iniciando agente`.
2. Digite sua pergunta no prompt `Qual a sua pergunta:`.
3. O agente processará a pergunta usando o GPT-4o-mini e retornará uma resposta em markdown, na persona de cantor.
4. O ciclo se repete, permitindo múltiplas perguntas na mesma sessão.
5. Para encerrar a conversa, digite um dos comandos abaixo (não diferencia maiúsculas/minúsculas):

```
exit
sair
cancelar
finalizar
```

O programa então finaliza a execução de forma limpa.

---

## 🧩 Estrutura do código

Abaixo está uma explicação geral de como o código está organizado:

```python
# 1. Importações
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

# 2. Carregamento das variáveis de ambiente
load_dotenv()

# 3. Configuração do agente
agente = Agent(
    description="voce é um cantor",
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)

print("Iniciando agente")

# 4. Loop principal de interação no terminal
while True:
    pergunta = input("Qual a sua pergunta:")
    if pergunta.lower() in ["exit", "sair", "cancelar", "finalizar"]:
        print("-" * 30)
        print("Finalizando agente 🤖")
        print("-" * 30)
        break
    else:
        agente.print_response(pergunta)
```

### Descrição das seções

| Seção                       | Função                                                                              |
|------------------------------|--------------------------------------------------------------------------------------|
| **Importações**              | Carrega as bibliotecas necessárias (Agno, dotenv, etc.)                              |
| **Carregamento do `.env`**   | Lê a chave da OpenAI de forma segura a partir do arquivo `.env`                       |
| **Configuração do agente**   | Define o modelo (GPT-4o-mini), a persona (cantor) e a formatação markdown das respostas |
| **Loop de interação**        | Mantém a conversa ativa no terminal até o usuário digitar um comando de saída          |

---

## 💬 Exemplos de uso

**Exemplo 1 — Pedindo uma letra de música**

```
Qual a sua pergunta: Crie uma letra curta sobre saudade
🎤 [O agente responde com uma letra original, em formato markdown]
```

**Exemplo 2 — Perguntando sobre técnica vocal**

```
Qual a sua pergunta: Como posso melhorar minha respiração ao cantar?
🎤 [O agente responde com dicas de técnica vocal e respiração]
```

**Exemplo 3 — Encerrando a sessão**

```
Qual a sua pergunta: sair
------------------------------
Finalizando agente 🤖
------------------------------
```

---

## 🛠️ Solução de problemas comuns

| Problema                                         | Possível causa                              | Solução                                                                 |
|--------------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------|
| `ModuleNotFoundError: No module named 'agno'`     | Dependência não instalada                    | Execute `pip install agno`                                               |
| `openai.AuthenticationError`                      | Chave de API inválida ou ausente             | Verifique se o arquivo `.env` existe e contém a chave correta            |
| Nenhuma resposta do agente / erro de conexão      | Falta de internet ou instabilidade na API    | Verifique sua conexão e o status da API em [status.openai.com](https://status.openai.com) |
| Variáveis do `.env` não são carregadas            | `python-dotenv` não instalado ou `load_dotenv()` ausente | Instale com `pip install python-dotenv` e confirme a chamada no código |
| Erro de versão do Python                          | Versão do Python desatualizada               | Atualize para Python 3.10 ou superior                                    |
| Créditos da API esgotados                         | Conta OpenAI sem saldo disponível            | Verifique o saldo em [platform.openai.com/usage](https://platform.openai.com/usage) |

---

## 👤 Autor

> _Preencha com suas informações:_
- Nome:
- GitHub:
- Contato:

---

## 📄 Licença

> _Defina a licença do projeto (ex.: MIT, Apache 2.0, GPL-3.0) ou deixe em aberto até decidir._

---

<p align="center">Feito com 💜 usando Python, Agno e OpenAI</p>