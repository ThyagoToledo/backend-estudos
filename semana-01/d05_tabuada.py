n = int(input("Tabuada de: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}") # Para cada valor de i, multiplica n por i e imprime o resultado

print()

print("Tabuada de 1 a 3")
print()
for a in range(1, 4):          # 'a' vai ser 1, depois 2, depois 3
    for b in range(1, 4):      # Para cada 'a', 'b' vai rodar de 1 até 3
        print(f"{a} x {b} = {a * b}")
    print()                    # Dá uma linha em branco para separar as tabuadas