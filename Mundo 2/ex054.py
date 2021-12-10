from datetime import date
atual = date.today().year

maior=0
menor=0
for cont in range(1,8):
    nasc = int(input("PESSOA Nº{} | DIGITE O ANO DE NASCIMENTO:".format(cont)))
    if atual-nasc >= 18:
        maior += 1
    else:
        menor += 1
print("MAIORES DE IDADE: {}".format(maior))
print("MENORES DE IDADE: {}".format(menor))