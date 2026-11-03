saldo = 1000.0

while True:
    opcao = int(input("1 - Saldo\n2 - Saque\n3 - Deposito\n4 - Exit\nEscolha uma opção: "))

    if opcao == 1:
        print(f"Seu saldo é: R${saldo:.2f}")
        
    elif opcao == 2:
        saque = float(input("Digite o valor de saque que deseja sacar: "))
        
        if saque > saldo:
            print(f"Operação negada! Saldo insuficiente. Você tem R${saldo:.2f} disponível.")
            
        elif saque <= 0:
            print("Operação negada! O valor do saque deve ser maior que zero.")
            
        else:
            saldo -= saque
            print(f"Saque de R${saque:.2f} realizado com sucesso!")
        
    elif opcao == 3:
        deposito = float(input("Digite o valor que deseja depositar: "))
        
        if deposito <= 0:
             print("Operação negada! O valor do depósito deve ser maior que zero.")
        else:
            saldo += deposito
            print(f"Depósito de R${deposito:.2f} realizado com sucesso!")
        
    elif opcao == 4:
        print("Saindo do sistema...")
        break