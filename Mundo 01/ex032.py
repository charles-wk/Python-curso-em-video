'''Um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''
from datetime import date
ano = int(input('Digite o ano: '))
if (ano == 0):
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))