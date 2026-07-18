# framework é tipo uma pasta de bibliotecas prontas, que facilitam a criação de agentes de IA

# ============================================================
# IMPORTAÇÕES - trazendo os frameworks/bibliotecas necessárias
# ============================================================

# Agent -> classe principal do agno, usada para criar um agente de IA
from agno.agent import Agent

# OpenAIChat -> classe que representa o modelo de IA da OpenAI que o agente vai usar
from agno.models.openai import OpenAIChat

# load_dotenv -> função que lê o arquivo .env e carrega as variáveis de ambiente
# (usamos isso para não deixar a chave da API exposta direto no código)
from dotenv import load_dotenv

# ============================================================
# CONFIGURAÇÃO INICIAL
# ============================================================

# executa a leitura do arquivo .env e carrega as variáveis (ex: OPENAI_API_KEY)
# sem isso, o agente não vai conseguir se autenticar na API da OpenAI
load_dotenv()

# ============================================================
# CRIAÇÃO DO AGENTE
# ============================================================

# aqui criamos o agente de IA, passando algumas configurações:
agente = Agent(
    description="voce é um cantor",       # define a "personalidade"/persona do agente
    model=OpenAIChat(id="gpt-4o-mini"),   # define qual modelo de IA será usado (gpt-4o-mini)
    markdown=True                          # faz o agente formatar as respostas em markdown
)

# mensagem só para avisar no terminal que o agente está pronto pra uso
print("Iniciando agente")

# ============================================================
# LOOP PRINCIPAL - conversa contínua com o agente
# ============================================================

# while True cria um loop infinito, ou seja, o programa fica perguntando
# sem parar, até que uma condição de saída seja atendida (break)
while True:

    # input() pausa o programa e espera o usuário digitar algo no terminal
    pergunta = input("Qual a sua pergunta:")

    # verifica se a pergunta digitada é um comando de saída
    # o .lower() transforma o texto digitado em minúsculo,
    # assim funciona tanto "Sair", "SAIR" quanto "sair"
    if pergunta.lower() in ["exit", "sair", "cancelar", "finalizar"]:

        # se caiu aqui, o usuário quer encerrar o programa
        print("-" * 30)                 # imprime uma linha de "-" só de estética/separador
        print("Finalizando agente 🤖")   # mensagem de despedida
        print("-" * 30)                 # outra linha separadora
        break                            # break interrompe o loop while, encerrando o programa

    else:
        # se não for comando de saída, o texto digitado é tratado como uma pergunta de verdade
        # agente.print_response() já faz duas coisas: chama a IA com a pergunta E imprime a resposta formatada
        agente.print_response(pergunta)
