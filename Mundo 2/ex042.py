'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

print('='*40)
print('Analisando Triângulo')
print('='*40)
r1 = float(input('Digite o comprimento da 1ª reta: '))
r2 = float(input('Digite o comprimento da 2ª reta: '))
r3 = float(input('Digite o comprimento da 3ª reta: '))

if r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2:
    print('É possível formar um triângulo ', end = '')
    if r1 == r2 == r3:
        print('equilátero △')

    elif r1 != r2 != r3 != r1:
            print('escaleno △')

    else:
        print('isósceles △')
else:
    print('Não é possível formar um triângulo △')