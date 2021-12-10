'''Um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.
Seu programa deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = date.today().year
confirm = str(input("Você já se alistou ao serviço militar [S/N]: "))
confirm = confirm.upper()

if confirm =="N":
    nasc = int(input("Digite o ano do seu nascimento: "))
    idade = ano-nasc

    if idade == 17:
        print("Falta {} ano para se alistar ao serviço militar.".format((idade-18)*-1))
    elif idade < 17:
        print("Faltam {} anos para se alistar ao serviço militar.".format((idade - 18) * -1))
    elif idade == 18:
        print("Já está na hora de você se alistar ao serviço militar.")
    elif idade == 19:
        print("Você está atrasado {} ano para se alistar ao serviço militar.".format(idade-18))
    else:
        print("Você está atrasado {} anos para se alistar ao serviço militar.".format(idade-18))

else:
    print("Parabéns, você já se alistou ao serviço militar!")