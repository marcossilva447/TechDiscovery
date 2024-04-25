# Criando dicionários

'''Um dicionário é uma coleção de pares chave-valor,
onde a chave é um identificador único para um valor, 
que pode ser acessado através da chave correspondente.'''

# Criando um dicionário vazio

dicionario = {}

# os valores de um dicionário são separados por vírgulas
# e cada par chave-valor é separado por dois pontos

#exemplo

pessoa = {'nome': 'Guilherme', 'idade': 29}

pessoa = dict(nome="Guilherme", idade=29) #está é uma forma de se criar um dicionário

pessoa["telefone"] = "3333-1234" # {"nome": "Guilherme", "Idade":28, "telefone": "3333-1234"}

# Acessando valores no dicionário

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"] # Guilherme
dados["idade"] # 28
dados["telefone"] # 3333-1234

dados["nome"] = "Maria" # alterando o valor da chave nome
dados["idade"] = 29 # alterando o valor da chave idade
dados["telefone"] = "9999-9999" # alterando o valor da chave telefone

dados # {'nome': 'Maria', 'idade': 29, 'telefone': '9999-9999'}

# Dicionários aninhados

# Dicionários podem armazenar qualquer tipo de objeto Python
# inclusive outros dicionários

'''contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "9999-9999"},
    "giovana@gmail.com": {"nome": "Giovana", "telefone": "8888-8888"}
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "7777-7777"}
}

contatos["giovana@gmail.com"]["telefone"] # 8888-8888

# iterar sobre um dicionário

for chave in dados:
    print(chave, dados[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# nome Guilherme
# idade 29
# telefone 9999-9999

# métodos de dicionários

# clear() - remove todos os itens do dicionário

dados.clear() # {}

# copy() - retorna uma cópia do dicionário

copia = contatos.copy()

# fromkeys() - retorna um dicionário com as chaves especificadas e o valor especificado

pessoas = {}.fromkeys(["nome", "idade"], "desconhecido") # {"nome": "desconhecido", "idade": "desconhecido"}

# get() - retorna o valor da chave especificada

pessoas.get("nome") # desconhecido

# items() - retorna uma lista contendo uma tupla para cada par chave-valor

pessoas.items() # dict_items([('nome', 'desconhecido'), ('idade', 'desconhecido')])
#ou
pessoas.items() # dict_items([('nome', 'desconhecido'), ('idade', 'desconhecido')])

# keys() - retorna as chaves do dicionário

pessoas.keys() # dict_keys(['nome', 'idade'])

# pop() - remove o item com a chave especificada

pessoas.pop("idade") # desconhecido

# popitem() - remove o último item inserido

pessoas.popitem() # ('nome', 'desconhecido')

# setdefault() - retorna o valor da chave especificada. Se a chave não existir, insere a chave com o valor especificado

pessoas.setdefault("nome", "Guilherme") # desconhecido
pessoas.setdefault("telefone", "9999-9999") # 9999-9999

# update() - atualiza o dicionário com os elementos especificados

pessoas.update({"nome": "Guilherme"}) # {'nome': 'Guilherme', 'telefone': '9999-9999'}


# values() - retorna uma lista de todos os valores no dicionário

pessoas.values() # dict_values(['Guilherme', '9999-9999'])


# in - verifica se a chave especificada existe no dicionário

"nome" in pessoas # True

# del - remove o item com a chave especificada

del pessoas["nome"] # {'telefone': '9999-9999'}

'''