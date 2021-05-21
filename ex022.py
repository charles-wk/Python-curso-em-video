'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras no total (sem considerar espaços)
Quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: '))
dividir = nome.split()
print('O nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('O nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Ao todo seu nome tem: {} letras' .format(len(''.join(dividir))))
print('O primeiro nome tem: {} letras'.format(len(dividir[0])))