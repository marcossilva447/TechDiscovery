class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # Método construtor
        self.cor = cor # Atributos: cor da bicicleta
        self.modelo = modelo # Atributos: modelo da bicicleta
        self.ano = ano  # Atributos: ano de fabricação
        self.valor = valor # Atributos: valor da bicicleta
        # usamos self para referenciar o objeto que está sendo criado
    
    def buzinar(self):
        print('BIBI')
    
    def parar(self):
        print('Freando a bicicleta')
    
    def pedalar(self):
        print('Pedalando a bicicleta')

    def __str__(self):
        return f'Bicicleta {self.modelo} {self.cor} {self.ano} {self.valor}'
    # Método mágico que retorna uma string com as informações da bicicleta

# Instanciando objetos da classe Bicicleta

b1 = Bicicleta('Azul', 'Caloi', 2020, 500.00)
print(b1)
b1.buzinar()
b1.parar()
b1.pedalar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('Vermelha', 'Monark', 2021, 700.00)
print(b2)
b2.pedalar()
 # A vantagem de usar classes é que podemos criar objetos com as mesmas características