import pickle

class Extrato:
    def receber_informacoes(self):
        # Abrir o arquivo extrato_file em modo de leitura binária
        with open('extrato_file', 'rb') as file:
            # Desserializar o objeto enviado pelo objeto Deposito.py
            informacoes = pickle.load(file)
        
        # Fazer algo com as informações recebidas
        # Por exemplo, imprimir na tela
        print(informacoes)

# Criar uma instância da classe Extrato
extrato = Extrato()

# Chamar o método receber_informacoes para receber as informações
extrato.receber_informacoes()