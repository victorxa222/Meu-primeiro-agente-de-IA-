# requests -> biblioteca usada para fazer requisições HTTP (conversar com APIs pela internet)
import requests

# ============================================================
# ENTRADA DO USUÁRIO
# ============================================================

# input() pausa o programa e espera o usuário digitar o CEP no terminal
# o texto digitado sempre vem como string (mesmo sendo números)
cep = input("digite seu cep (apenas numeros):")

# ============================================================
# MONTANDO A URL DA API
# ============================================================

# f"..." é uma f-string: permite inserir variáveis dentro do texto usando {}
# aqui montamos a URL da API ViaCEP, trocando {cep} pelo valor digitado
# ex: se o usuário digitar 01001000, a url vira:
# https://viacep.com.br/ws/01001000/json/
url = f"https://viacep.com.br/ws/{cep}/json/"

# ============================================================
# FAZENDO A REQUISIÇÃO PARA A API
# ============================================================

# requests.get() faz uma requisição do tipo GET, ou seja, busca/lê informações da API
# GET  -> serve apenas para LEITURA de dados (não altera nada no servidor)
# POST -> serve para ENVIAR/CRIAR dados no servidor (ex: cadastrar algo)
# PUT/PATCH -> servem para ATUALIZAR dados existentes
# DELETE -> serve para APAGAR dados
dados = requests.get(url)

# ============================================================
# CONVERTENDO A RESPOSTA PARA JSON
# ============================================================

# a resposta da API vem em um formato bruto (texto), então precisamos converter
# .json() transforma essa resposta em um dicionário Python, que é mais fácil de manipular
# (sempre usa parênteses () pois é um método, uma "ação" sendo executada na variável)
endereco = dados.json()

# ============================================================
# EXIBINDO O RESULTADO
# ============================================================

# endereco['logradouro'] e endereco['localidade'] acessam valores específicos
# dentro do dicionário retornado pela API (nome da rua e nome da cidade)
# usando f"..." não precisamos concatenar com + para juntar texto e variável,
# basta colocar a variável dentro de {}
print(f"Você mora na rua {endereco['logradouro']} e mora na cidade {endereco['localidade']}")
