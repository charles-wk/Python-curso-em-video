'''Um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
para salários superiores a R$1.250.00 calcule um aumento de 10%
Pra inferiores ou iguais o aumento é de 15%'''

salario = float(input('Digite seu salário: R$'))

if (salario > 1250):
    aumento = (10 * salario) / 100
    print('O seu aumento será de: R${}'.format(aumento))
    print('Novo salário: R${}'.format(aumento+salario))
else:
    aumento = (15 * salario) / 100
    print('O seu aumento será de: {}'.format(aumento))
    print('Novo salário: R${}'.format(aumento+salario))
