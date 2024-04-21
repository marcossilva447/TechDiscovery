import Deposito.py
import Saque.py

opcao = input('''Escolha a operação desejada: 
              1 - Depósito
              2 - Saque
              3 - Extrato
              4 - Sair
              ''')

if opcao == 1:
    operacao = Deposito.py.operacao_deposito()
elif opcao == 2:
    operacao = Saque.py.operacao_saque()
