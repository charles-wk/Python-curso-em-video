'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. '''
totalpar = 0
tuplanum = (int(input('Digite um número: ')),
            int(input('Digite outro número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite o último número: ')))
print(f'O valor 9 aparece {tuplanum.count(9)} vezes')
if tuplanum.count(3) == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 aparece na {tuplanum.index(3)+1}ª posição')
print('Os valores pares digitados foram: ', end='')
for c in tuplanum:
    if c % 2 == 0:
        print(c, end=' ')


