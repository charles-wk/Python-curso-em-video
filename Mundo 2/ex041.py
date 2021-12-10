'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM.
- Até 14 anos: INFANTIL.
- Até 19 anos: JUNIOR.
- até 20 anos: SÊNIOR.
- Acima: MASTER.'''

from datetime import date
atual = date.today().year
print("_"*40)
print("ANALISADOR DE CATEGORIAS")
print("_"*40)

ano = int(input("DIGITE SEU ANO DE NASCIMENTO: "))
idade = atual-ano
print("_"*40)

if idade <= 9:
    print("IDADE:{} ANOS | CATEGORIA MIRIM".format(idade))

elif idade > 9 and idade <= 14:
    print("IDADE:{} | CATEGORIA INFANTIL".format(idade))

elif idade > 14 and idade <= 19:
    print("IDADE:{} | CATEGORIA JUNIOR".format(idade))

elif idade > 19 and idade <= 25:
    print("IDADE:{} | CATEGORIA SÊNIOR".format(idade))

else:
    print("IDADE:{} | CATEGORIA MASTER".format(idade))