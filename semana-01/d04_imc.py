peso = float(input("Digite o peso em KG(Kilo Gramas):"))
altura = float(input("Digite a altura em M(metros):"))

imc = (peso / altura **2)

if imc < 18.5:
    print(f"O IMC: {imc}, se encontra Abaixo do peso!")
elif imc >= 18.5 and imc <=24.9:
    print(f"O IMC: {imc}, se econtra Normal.")    
elif imc >= 25 and imc <=29.9:
    print(f"O IMC: {imc}, se encontra em Sobrepeso!")
else:
    print(f"O IMC: {imc}, se encontra em OBESIDADE!!!")