segredo = 42
tentativas = 0

while tentativas < 5:
    chute = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if chute == segredo:
        print(f"Acertou em {tentativas} tentativa(s)!")
        break
    print("maior" if segredo > chute else "menor")
else:
    print("Acabaram as tentativas")