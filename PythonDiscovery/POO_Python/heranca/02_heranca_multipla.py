'''class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self): # Método mágico que retorna uma representação em string do objeto
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


class Mamifero(Animal):
    def __init__(self, nro_patas, cor_pelo): # Sobrescrevendo o método __init__ da classe Animal
        self.cor_pelo = cor_pelo
        super().__init__(nro_patas)

class Ave(Animal):
    def __init__(self, nro_patas):
        super().__init__(nro_patas)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(4, "Preto")
print(gato) # 4

# 06:08

'''
class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())

class Bar(Foo):
    def hello(self):
        return super().hello()
    
bar = Bar()
bar.hello() # bar