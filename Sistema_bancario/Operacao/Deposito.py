def operacao_deposito():
    valor = float(input("Digite o valor do depósito: "))
    if valor <= 0:
        print("Operação inválida.")
        print("Sessão encerrada.")
    else:
        confirmacao = input(f"Valor digitado: {valor}. Confirma? S/N")
        if confirmacao == "S":
            print("Coloque o dinheiro na área indicada.")
            print("Aguarde a contagem do dinheiro.")
            print("Dinheiro contado com sucesso.")
        elif confirmacao == "N":
            valor += float(input("Digite o valor do depósito: "))
            print("Coloque o dinheiro na área indicada.")
            print("Aguarde a contagem do dinheiro.")
            print("Dinheiro contado com sucesso.")
        else:
            print("Opção inválida.")
            operacao_deposito()
    return valor

operacao_deposito()

def enviar_valor_extrato(valor):
    with open("Extrato.py", "a") as extrato_file:
        extrato_file.write(str(valor) + "\n")


