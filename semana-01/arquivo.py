# --- E01.2 (N2): Nome, frase e as 4 operações ---
print("Thyago")
print("Estudando backend com Python")
print(f"(12 + 8) * 3 = {(12 + 8) * 3}")
print(f"17 / 4 = {17 / 4}")
print(f"17 // 4 = {17 // 4}")
print(f"17 % 4 = {17 % 4}")

# --- E01.4 (N4): Usando sep e end ---
# 1. Duas palavras/frases em linhas diferentes com um único print()
print("Linha 1", "Linha 2", sep="\n")

# 2. Imprimindo sem quebra de linha ao final (continua na mesma linha)
print("Sem quebra", end="")
print(" -> continua na mesma linha")