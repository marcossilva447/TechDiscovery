class Cachorro:
    def __init__(self, nome, raca, idade): #construtor
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def __del__(self): #destrutor
        print('Removendo a instância da classe')
    
    def latir(self):
        print('Au au...')
    


def criar_cachorro():
    c1 = Cachorro('Rex', 'vira-lata', 2)
    print(c.nome)

c = Cachorro('Rex', 'vira-lata', 2)
c.latir()

del c

# a utilização do destrutor é opcional, mas é uma boa prática para liberar recursos
# que não estão mais sendo utilizados