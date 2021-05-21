'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome'''

nome = str(input('Digite seu nome: ')).upper()
print ('O nome tem Silva? {}'.format('SILVA' in nome))