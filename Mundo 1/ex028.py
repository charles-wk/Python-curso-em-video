'''Um programa que o computador pense em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''

import random

adivinhar = int(input('De 1 a 5, tente adivinhar o numero que o computador está pensando: '))
sorteio = random.choice([1,2,3,4,5])

if adivinhar == sorteio:
    print('Você venceu! O número que o computador esta pensando é: {}'.format(sorteio))
else:
    print('Você perdeu! O número que o computador está pensando é: {}'.format(sorteio))