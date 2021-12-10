'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
m = h = f = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    i = int(input('Digite sua idade: '))
    s = str(input('Digite seu sexo [F/M]: '))
    print('-' * 30)
    r = str(input('Quer continuar [S/N]: '))
    print('-' * 30)
    if i > 18:
        m += 1
    if s in 'Mm':
        h += 1
    if s in 'Ff' and i < 20:
        f += 1
    if r in 'Nn':
        break
print(f'Pessoas com mais de 18 anos: {m}')
print(f'Homens cadastrados: {h}')
print(f'Mulheres com menos de 20 anos: {f}')
