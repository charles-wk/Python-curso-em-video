'''  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla.'''
import random
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
c = 0
print('Os valores sorteados foram: ', end='')
n1 = 1
n2 = 9
while c < 5:
    n = random.choice(numeros)
    print(n, end=' ')
    c+=1
    if n > n1:
        maior = n
        n1 = n
    elif n < n2:
        menor = n
        n2 = n
print(f'\nO maior número é: {maior}')
print(f'O menor número é: {menor}')

'''Código do professor
from random import radint
numeros = (radint(1,10), radint(1,10), radint(1,10),
    radint(1,10), radint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')'''
