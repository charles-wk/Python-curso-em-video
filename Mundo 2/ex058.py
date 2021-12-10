'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.'''
import random
adv = 0
srt = 1
plpt = 0
while adv != srt:
    adv = int(input('De 1 a 10, qual numero o computador está pensando: '))
    srt = random.choice(1,10)
    if adv != srt:
        if adv > srt:
            print('Menos...')
        else:
            print('Mais...')
        plpt += 1
        print('Você errou! Tente de novamente.')
    else:
        print('Você acertou! O número que o computador esta pensando é {}'.format(srt))
        print('Você necessitou de {} palpites para adivinhar.'.format(plpt))