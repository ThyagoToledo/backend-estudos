soma = 0
numero = 1

print("Digite 0 para sair")

while numero != 0:
    numero = int(input("digite um número: "))
    soma += numero

print(f"A soma dos numeros digitados é: {soma}")