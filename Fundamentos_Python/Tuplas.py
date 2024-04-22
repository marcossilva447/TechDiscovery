'''Tuplas são estruturas de dados semelhantes às listas, 
mas imutáveis.
Podemos criar tuplas através da classe tuple ou utilizando
parênteses, separando os valores por vírgula.
'''

# Exemplo

frutas = ("laranja", "maca", "uva")
letras = tuple("python")
numeros = tuple([1,2,3,4,5])
pais = ("Brasil",)

# é uma boa prática adicionar uma vírgula ao final de uma tupla com um único elemento

# Acesso direto --> através do índice --> índice contado a partir do zero.

frutas[0] #Laranja
frutas[2] #Uva

# Exemplo de matriz (tupla aninhada)

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

# Acessando os valores na matriz

matriz[0] #(1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2

# usar tuplas garante que os valores serão imutáveis

#fatiamento de tuplas é semelhante ao de listas

# Métodos da classe tuple

# count() --> retorna o número de vezes que um valor aparece na tupla

numeros.count(1) # 1
numeros.count(10) # 0

# index() --> retorna o índice da primeira ocorrência de um valor

numeros.index(1) # 0
numeros.index(10) # ValueError: 10 is not in list

# len() --> retorna o número de elementos da tupla

len(numeros) # 5
