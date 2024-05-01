'''JOão tem uma bicicletaria e gostaria de registrar as vendas 
de suas bicicletas. Crie um programa onde João informe: cor,
modelo, ano e valor da bicicleta vendida. Uma bicicleta pode:
buzinar, parar e correr. Adicione esses comportamentos!'''

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    '''a notação de métodos é muito parecida com funções, mas a diferença é que métodos são funções 
    que pertencem a uma classe e funções são independentes'''

    def buzinar(self):
        print('Plim plim...')

    def parar(self):
        print('Parando...')
        print('Bicicleta parada!')

    def correr(self):
        print('Vrummmm...')

    def __str__(self): #retorna uma string para o seu objeto
        return f'''Bicicleta: cor = {self.cor} modelo = {self.modelo} 
        fabricação = {self.ano} preço = {self.valor}'''
    
    # def __str__(self):
    #    return f'(self.__class__.__name__): {', '.join[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}'

   
b1 = Bicicleta('vermelha', 'caloi', 2020, 500.00) # Instanciando um objeto
print(b1) # Bicicleta.__str__(b1)
#chamando os métodos

b1.buzinar() # Bicicleta.buzinar(b1)
b1.correr() # Bicicleta.correr(b1)
b1.parar() # Bicicleta.parar(b1)

#print(b1.cor, b1.modelo, b1.ano, b1.valor) # Acessando os atributos

b2 = Bicicleta('azul', 'monark', 2021, 600.00) # Instanciando um objeto
print(b2) # Bicicleta.__str__(b1)

