#framework é tipo uma pastas de bibliotecas 

#importanto os frameworks necessarios para o projeto
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

#ler .env
load_dotenv()

agente = Agent (
    description="voce é um cantor",
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)

print("Iniciando agente")

while True:
    pergunta = input("Qual a sua pergunta:")
    if pergunta.lower() in ["exit","sair","cancelar","finalizar"]:#o .lower serve para deixar a pergunta do usuario tudo minusculo, só assim vai funcionar o comando "sair"
        print("-" * 30)
        print("Finalizando agente 🤖")
        print("-" * 30)
        break
    else:
        agente.print_response(pergunta)