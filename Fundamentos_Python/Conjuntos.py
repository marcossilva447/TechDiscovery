'''Um set ou conjunto é uma coleção que não possui objetos
repetidos, ou seja, não possui elementos duplicados.
Usamos sets para representar conjuntos matemáticos ou 
eliminar itens duplicados de uma lista.'''

# Criando um conjunto
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}
set("abacaxi") # {'a', 'b', 'c', 'i', 'x'}
set("palio", "gol", "celta", "palio") # {'palio', 'gol', 'celta'}

linguagens = {"Python", "Java", "C", "C++", "Python"} #sintaxe pouco usada
print(linguagens) # {'Java', 'Python', 'C', 'C++'}

# Acessando os dados --> é necessário converter o set em uma lista

numeros = {1, 2, 3, 4, 5}
numeros = list(numeros)
numeros[0] # 1

# É possível percorrer um set utilizando um loop for
for numero in numeros:
    print(numero)

# Função enumerate
# A função enumerate retorna uma tupla com o índice e o valor do elemento

for indice, numero in enumerate(numeros):
    print(f"O número {numero} está na posição {indice}")

# Métodos da classe set

#{}.union() --> retorna a união de dois conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto1.union(conjunto2) # {1, 2, 3, 4, 5}

#{}.intersection() --> retorna a interseção de dois conjuntos
conjunto1.intersection(conjunto2) # {3}

#{}.difference() --> retorna a diferença entre dois conjuntos
conjunto1.difference(conjunto2) # {1, 2}

#{}.symmetric_difference() --> retorna a diferença simétrica entre dois conjuntos
conjunto1.symmetric_difference(conjunto2) # {1, 2, 4, 5}

#{}.add() --> adiciona um elemento ao conjunto
conjunto1.add(4) # {1, 2, 3, 4}

#{}.remove() --> remove um elemento do conjunto
conjunto1.remove(4) # {1, 2, 3}

#{}.pop() --> remove um elemento aleatório do conjunto
conjunto1.pop() # {2, 3}

#{}.clear() --> remove todos os elementos do conjunto
conjunto1.clear() # {}

#{}.copy() --> retorna uma cópia do conjunto
conjunto1 = {1, 2, 3}
conjunto2 = conjunto1.copy()
print(conjunto2) # {1, 2, 3}

#{}.issubset() --> verifica se um conjunto é subconjunto de outro
conjunto1.issubset(conjunto2) # True

#{}.issuperset() --> verifica se um conjunto é superconjunto de outro
conjunto2.issuperset(conjunto1) # True

#{}.isdisjoint() --> verifica se dois conjuntos são disjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
conjunto1.isdisjoint(conjunto2) # True

#{}.update() --> atualiza um conjunto com a união de dois conjuntos
conjunto1.update(conjunto2) # {1, 2, 3, 4, 5, 6}

#{}.intersection_update() --> atualiza um conjunto com a interseção de dois conjuntos
conjunto1.intersection_update(conjunto2) # {4, 5, 6}

#{}.difference_update() --> atualiza um conjunto com a diferença de dois conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto1.difference_update(conjunto2) # {1, 2}

#{}.symmetric_difference_update() --> atualiza um conjunto com a diferença simétrica de dois conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto1.symmetric_difference_update(conjunto2) # {1, 2, 4, 5}

#{}.discard() --> remove um elemento do conjunto
conjunto1.discard(4) # {1, 2, 5}


