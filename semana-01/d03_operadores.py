# Arquivo: d03_operadores.py | Data: 16/10/2026

# Testes com numero inteiro (paridade e divisibilidade)
n = int(input("Digite um numero inteiro: "))
print("E par?", n % 2 == 0)
print("E multiplo de 3?", n % 3 == 0)
print("E par e multiplo de 3?", n % 2 == 0 and n % 3 == 0)

# Conversao de segundos para horas, minutos e segundos
segundos = int(input("Digite o total de segundos: "))
horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segs = resto % 60
print(f"{horas}h {minutos}min {segs}s")

# Tabela de operacoes aritmeticas e comparacoes
a = int(input("Digite o primeiro numero (a): "))
b = int(input("Digite o segundo numero (b): "))

print(f"Soma: {a + b}")
print(f"Diferenca: {a - b}")
print(f"Produto: {a * b}")
print(f"Divisao real: {a / b}")
print(f"Divisao inteira: {a // b}")
print(f"Resto da divisao: {a % b}")
print(f"Potencia: {a ** b}")
print(f"a == b: {a == b}")
print(f"a > b: {a > b}")
print(f"a e divisivel por b: {a % b == 0}")
