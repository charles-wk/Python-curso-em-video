'''Crie um programa que faça o computador jogar Jokenpô com você.'''

import random

pc = random.choice(['PEDRA','PAPEPL', 'TESOURA'])
print("-"*30)
print("JOKENPÔ - CONTRA O COMPUTADOR")
print("-"*30)
print("[] PEDRA")
print("[] PAPEL")
print("[] TESOURA")
user = str(input("DIGITE SUA OPÇÃO: "))
user = user.upper()
print("-"*30)
pc = random.choice(['PEDRA','PAPEL', 'TESOURA'])

#---empate
if user == pc:
    print("COMPUTADOR: {}".format(pc))
    print("VOCÊ: {}".format(user))
    print("EMPATE!")

#---user ganha
elif user == 'PEDRA' and pc == 'TESOURA':
    print("COMPUTADOR: {}".format(pc))
    print("VOCÊ: {}".format(user))
    print("VOCÊ GANHOU!")

elif user == 'PAPEL' and pc == 'PEDRA':
    print("COMPUTADOR: {}".format(pc))
    print("VOCÊ: {}".format(user))
    print("VOCÊ GANHOU!")

elif user == 'TESOURA' and pc == 'PAPEL':
    print("COMPUTADOR: {}".format(pc))
    print("VOCÊ: {}".format(user))
    print("VOCÊ GANHOU!")

#---pc ganha
elif pc == 'PEDRA' and user == 'TESOURA':
    print("COMPUTADOR: {}".format(pc))
    print("VOCÊ: {}".format(user))
    print("VOCÊ PERDEU!")

elif pc == 'PAPEL' and user == 'PEDRA':
    print("COMPUTADOR: {}".format(pc))
    print("VOCÊ: {}".format(user))
    print("VOCÊ PERDEU!")

elif pc == 'TESOURA' and user == 'PAPEL':
    print("COMPUTADOR: {}".format(pc))
    print("VOCÊ: {}".format(user))
    print("VOCÊ PERDEU!")

else:
    print('OPÇÃO INVÁLIDA - TENTE NOVAMENTE!')





