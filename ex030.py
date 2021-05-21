'''Um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR'''

num = float(input('Digite um número: '))

if num % 2 == 0:
    print('{:.1f} é par!'.format(num))
else:
    print('{:.1f} é ímpar!'.format(num))