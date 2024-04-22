# Lista é uma sequência que pode armazenar qualquer tipo de objeto
# Listas são mutáveis, ou seja, podem ser alteradas
# Listas são representadas por colchetes []

# Criando uma lista
''' Uma lista pode ser declarada por um método construtor list,
a função range() ou por colchetes [] '''

# Exemplo lista com elementos declarados

frutas = ["laranja", "maca", "uva"]

# Exemplo lista vazia

pessoas = []

# Exemplo usando o construtor list

letras = list("python") #cada letra da string será um elemento (elemento iterável)

# Exemplo usando a função range

numeros = list(range(10)) #gerará número de 0 a 9

# lista com múltiplos elementos

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

# Acesso direto --> através do índice --> índice contado a partir do zero.

frutas[0] #Laranja
frutas[2] #Uva

# é possível usar índices negativos, resultará na seleção da direita para esquerda

# Lista aninhadas podem ser usadas para representar matrizes bidimensionais

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

# Acessando os valores na matriz

matriz[0] #[1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c" 

# Fatiamento de listas --> podemos extrair um conjunto de valores de uma sequência
# Sintaxe:

lista = ["p","y","t","h","o","n"]
lista[2:] # ["t","h","o","n"]
lista[1:3] # ["y","t"]
lista[0:3:2] # ["p","t"]
lista[::] # ["p","y","t","h","o","n"]
lista[::-1] # ["n","o","h","t","y","p"]

# a posição que você coloca no final não é retornada

# Iterar listas --> for

carros =  ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# Função enumerate --> quando é necessário saber qual o índice do objeto 

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Compreensão de listas --> criar uma lista com base nos valores de outra lista

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# fazendo com compreensão de listas

pares = [numero for numero in numeros if numero % 2 == 0] # % é mod, ou resto da divisão

# Modificando valores com compreensão 

quadrado = [numero ** 2 for numero in numeros]

# Métodos da classe list

# [].append

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]

# [].clear

lista = [1, "Python", [40, 30, 20]]
print(lista) # [1, "Python", [40, 30, 20]]
lista.clear()
print(lista) # []

# [].copy

lista = [1, "Python", [40, 30, 20]]
lista.copy()
print(lista) # [1, "Python", [40, 30, 20]] --> não altera a lista original

# [].count

cores = ["azul", "verde", "amarelo", "azul", "vermelho", "azul"]
cores.count("azul") # 3
cores.count("preto") # 0

# [].extend
linguagens = ["python", "java", "c"]
print(linguagens) # ["python", "java", "c"]

linguagens.extend(["ruby", "javascript"])
print(linguagens) # ["python", "java", "c", "ruby", "javascript"]

# [].index retorna a primeira ocorrência na lista
liguagens = ["python", "java", "c"]
print(linguagens.index("python")) # 0
print(linguagens.index("c")) # 2

# [].pop remove o último elemento da lista
linguagens = ["python", "java", "c"]
linguagens.pop()
print(linguagens) # ["python", "java"]
linguagens.pop(0) # remove o primeiro elemento

# [].remove remove a primeira ocorrência do valor
linguagens = ["python", "java", "c"]
linguagens.remove("java")
print(linguagens) # ["python", "c"]

# [].reverse inverte a ordem dos elementos
linguagens = ["python", "java", "c"]
linguagens.reverse()
print(linguagens) # ["c", "java", "python"]

# [].sort ordena a lista
numeros = [10, 5, 3, 8, 4]
numeros.sort()
print(numeros) # [3, 4, 5, 8, 10]

# [].sort(reverse=True) ordena a lista em ordem decrescente
numeros = [10, 5, 3, 8, 4]
numeros.sort(reverse=True)
print(numeros) # [10, 8, 5, 4, 3]

# [].sort(key=função) ordena a lista de acordo com a função
def funcao_ordenacao(valor):
    return valor % 2

numeros = [10, 5, 3, 8, 4]
numeros.sort(key=funcao_ordenacao)
print(numeros) # [10, 8, 4, 5, 3]

# função lambda --> função anônima que pode ser passada como argumento
numeros = [10, 5, 3, 8, 4]
numeros.sort(key=lambda x: x % 2)
print(numeros) # [10, 8, 4, 5, 3]

# len() --> retorna o tamanho da lista
numeros = [10, 5, 3, 8, 4]
print(len(numeros)) # 5

# max() --> retorna o maior valor da lista
numeros = [10, 5, 3, 8, 4]
print(max(numeros)) # 10

# min() --> retorna o menor valor da lista
numeros = [10, 5, 3, 8, 4]
print(min(numeros)) # 3

# sorted() --> retorna uma nova lista ordenada
numeros = [10, 5, 3, 8, 4]
print(sorted(numeros)) # [3, 4, 5, 8, 10]


