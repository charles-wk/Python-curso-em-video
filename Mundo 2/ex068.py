'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.'''
import random
v = 0
while True:
    n = int(input("Digite um valor: "))
    pi = str(input('Par ou Ímpar [P/I]: '))
    pc = random.choice([0, 11])
    s = n+pc
    if pi in 'pP':
        if s % 2 == 0:
            print(f'O computador jogou {pc} e você {n}. Total {s}, Par')
            print('Você ganhou!')
            v += 1
        else:
            print(f'O computador jogou {pc} e você {n}. Total {s}, ímpar')
            print('Você perdeu!')
            print(f'Total de vitórias: {v}')
            break
    elif pi in 'iI':
        if s % 2 != 0:
            print(f'O computador jogou {pc} e você {n}. Total {s}, Ímpar')
            print('Você ganhou!')
            v += 1
        else:
            print(f'O computador jogou {pc} e você {n}. Total {s}, Par')
            print('Você perdeu!')
            print(f'Total de vitórias: {v}')
            break
