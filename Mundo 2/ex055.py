maior = 0
menor = 0
comp = 0
peso = float(input("PESSOA Nº1 | DIGITE O PESO: "))
#Invés de uma comparação antes do código, poderia apenas ter verificado o primeiro laço (if cont == 1:)
if peso > comp:
    maior = peso
    menor = peso

for cont in range(2,5+1):
    peso = float(input("PESSOA Nº{} | DIGITE O PESO: ".format(cont)))

    if peso > maior:
            maior = peso
    elif peso < menor:
            menor = peso
print("MAIOR PESO: {}". format(maior))
print ("MENOR PESO: {}".format(menor))

'''Código do professor

maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))'''