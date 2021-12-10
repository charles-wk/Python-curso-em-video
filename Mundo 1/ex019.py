#Faça um programa que ajude o professor, lendo o nome dos alunos e escrevendo o nome escolhido para apagar o quadro.
from random import choice, random
aluno = random.choice(['André', 'Luiz', 'Fabio', 'Carlos'])
print('O aluno sorteado para apagar o quadro foi: {}'.format(aluno))
