'''Faça um programa que leia um número
e mostre na tela os decimais

num = str(input('Digite um número inteiro de 0 a 9999: '))
num = num.split()
print('A unidade é: {}'.format(num[0][3]))
print('A dezena é: {}'.format(num[0][2]))
print('A centena é: {}'.format(num[0][1]))
print('O milhar é: {}'.format(num[0][0]))'''

num = int(input('Digite um número inteiro de 0 a 9999: '))
print ('A unidade é: {}'.format(num // 1 % 10))
print('A dezena é: {}'.format(num // 10 % 10))
print('A centena é: {}'. format(num // 100 % 10))
print('O milhar é: {}'.format(num // 1000 % 10))