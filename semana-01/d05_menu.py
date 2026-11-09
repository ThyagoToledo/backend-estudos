while True:
    print("Menu interativo")
    print()
    opcao = input(f"1) Dizer ola\n2) Contar de 1 ate N\n3) Somar numeros ate 0\n0) Sair\nEscolha: ")
    print()
    
    if opcao == "1":
        print("Olá! Seja bem-vindo.")
    elif opcao == "2":
        n = int(input("Contar até quanto? "))
        for i in range(1, n + 1):
            print(i, end=" ")
            print()
    elif opcao == "3":
        soma = 0
        while True:
            numero = int(input("Digite um numero (0para parar): "))
            if numero == 0:
                break
            soma += numero
        print(f"Soma total: {soma}")
    elif opcao == "0":
        print("Saindo do programa...")
        break
    
    else:
        print("opção invalida.")