def operacao_saque():
    valor = float(input("Digite o valor do saque: "))
    confirmacao = input(f"Valor digitado: {valor}. Confirma? S/N")
    if confirmacao == "S":
        print("Aguarde a contagem do dinheiro.")
        print("Dinheiro contado com sucesso.")
        print("Retire o dinheiro na área indicada.")
    else:
        print("Repita a operação.")
        operacao_saque()
    return valor # Retorna o valor do saque

operacao_saque() # Teste da função