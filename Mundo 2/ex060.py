'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

n = int(input("Digite o número que deseja fatorar: "))
c = n-1
f = n*c
print("{}! = {} x {} ".format(n, n, c), end='')
while c != 1:
    c -= 1
    f *= c
    print("x {} ".format(c), end='')
print("= {}".format(f))

'''Código professor:
from math import factorial
n = int(input('Digite o número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''
