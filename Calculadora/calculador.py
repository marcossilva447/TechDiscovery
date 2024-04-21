while True:
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == "5":
        print("Encerrando a calculadora...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = num1 + num2
        print("Resultado: ", resultado)
    elif opcao == "2":
        resultado = num1 - num2
        print("Resultado: ", resultado)
    elif opcao == "3":
        resultado = num1 * num2
        print("Resultado: ", resultado)
    elif opcao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado: ", resultado)
        else:
            print("Erro: Divisão por zero!")
    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")