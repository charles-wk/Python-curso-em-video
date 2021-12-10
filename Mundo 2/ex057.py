'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = 'M'
while sexo != 'M' or sexo != 'F':
    sexo = str(input("DIGITE SEU SEXO [M/F]: ")).upper()
    if sexo == 'M':
        print('Seu sexo é masculino!')
        break
    elif sexo == 'F':
        print('Seu sexo é feminino!')
        break
    elif sexo != 'M' and sexo != 'F':
        print('Houve um erro, por favor comece novamente!')


'''Codigo professor

sexo = input('Informe seu sexo: [M/F] ')
while sexo not in 'MmFf:
    sexo = inpu('Dados inválidos. Por favor, informe seu sexo: ).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
'''