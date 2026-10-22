# Arquivo: d02_perfil.py | Data: 15/10/2026

# Perfil do usuario
nome = input("Digite seu nome: ")
ano = int(input(f"{nome}, em qual ano voce nasceu? "))

idade = 2026 - ano

print(f"Ola, {nome}! Em 2026 voce faz {idade} anos.")

# Calculo da media aceitando virgula ou ponto
entrada1 = input("Digite a primeira nota: ").replace(",", ".")
entrada2 = input("Digite a segunda nota: ").replace(",", ".")

nota1 = float(entrada1)
nota2 = float(entrada2)
media = (nota1 + nota2) / 2

print(f"Media calculada: {media:.2f}")
