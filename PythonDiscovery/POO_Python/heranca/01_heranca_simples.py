class Veiculo:
    def __init__(self, cor, placa, eixos):
        self.cor = cor
        self.placa = placa
        self.eixos = eixos

    def ligar_motor(self):
        print('Ligando motor...')

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

#class Caminhao(Veiculo):
    #def __init__(self, carregado): # Sobrescrevendo o método __init__ da classe Veiculo
    #    sef.carregado = carregado

    #def esta_carregado(self):
    #    print(f'{"Estou" if self.carregado else "Não estou"} carregado')


# moto = Motocicleta() # TypeError: __init__() missing 3 required positional arguments: 'cor', 'placa', and 'eixos'
moto = Motocicleta('preta', 'ABC-1234', 2) # Instanciando um objeto da classe Motocicleta
print(moto)

carro = Carro('vermelho', 'XYZ-9876', 4) # Instanciando um objeto da classe Carro
carro.ligar_motor() # Ligando motor...

#caminhao = Caminhao('branco', 'DEF-4567', 6) # Instanciando um objeto da classe Caminhao
#caminhao.ligar_motor() # Ligando motor...
#caminhao.esta_carregado()   # Não estou carregado


carro.esta_carregado() # AttributeError: 'Carro' object has no attribute 'esta_carregado'

# A classe Carro não possui o método esta_carregado, pois este método foi definido apenas na classe Caminhao
# Para que a classe Carro possa ter acesso a este método, é necessário que a classe Carro herde da classe Caminhao


# método super()
# super.__init__() é um método que permite chamar o método __init__() da classe pai