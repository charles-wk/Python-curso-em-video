'''Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece última vez'''

frase = str(input('Digite uma frase: ')).strip().upper()
print ('A letra "A" aparece: {} vezes'.format(frase.count('A')))
print ('A primeira posiçaõ que ela aparece: {}'.format(frase.find('A')+1))
print('A última posição que ela aparece: {}'.format(frase.rfind('A')+1))