'''Um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo'''

print('='*40)
print('Analisando Triângulo')
print('='*40)
r1 = float(input('Digite o comprimento da 1ª reta: '))
r2 = float(input('Digite o comprimento da 2ª reta: '))
r3 = float(input('Digite o comprimento da 3ª reta: '))

if (r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2):
    print('△ É possível formar um triângulo △')
else:
    print('△ Não é possível formar um triângulo △')