import deposito.py

opcao = input('''Escolha a operação desejada: 
              1 - Depósito
              2 - Saque
              3 - Transferência
              4 - Saldo
              5 - Sair
              ''')

if opcao == 1:
    operacao = deposito.py.operacao_deposito()