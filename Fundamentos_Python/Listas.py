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