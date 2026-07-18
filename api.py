import requests 

cep = input("digite seu cep (apenas numeros):")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)# get serve apenas para leitura da api, como a url usada
                         # post serve para alterar algo na api

endereco = dados.json()#tm que abrir e fechar() depois de colocar qual tipo é a variavel, se é json, etc 

print(f"Você mora na rua {endereco['logradouro']} e mora na cidade {endereco['localidade']}") #quando tem o f"..." nao precisa colocar " , " para continuar a frase

