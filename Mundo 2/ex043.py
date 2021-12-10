'''Uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

print("-"*35)
print("CALCULADORA DE IMC")
print("-"*35)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura**2)
#Truncando imc
t = 2 #numero de casas desejadas
imc = int(imc*10**t)/10**t
print(imc)

if imc < 18.50:
    print("IMC: {:.2f} - ABAIXO DO PESO!".format(imc))

elif imc > 18.50 and imc < 25.00:
    print("IMC: {:.2f} - PESO IDEAL!".format(imc))

elif imc > 25.00 and imc <= 30.00:
    print("IMC: {:.2f} - SOBREPESO!".format(imc))

elif imc > 30.00 and imc <= 40.00:
    print("IMC: {:.2f} - OBESIDADE!".format(imc))

else:
    print("IMC: {:.2f} - OBESIDADE MÓRBIDA! CUIDADO!".format(imc))