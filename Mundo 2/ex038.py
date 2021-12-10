'''Um programa que leia dois números e compare-os, mostrando uma mensagem
 -O primeiro valor é maior.
 -O segundo valor é maior.
 -Não existe valor maior, os dois são iguais.'''

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

if (v1 > v2):
    print("O PRIMEIRO valor {} é o maior.".format(v1))
elif (v2 > v1):
    print("O SEGUNDO valor {} é o maior.".format(v2))
else:
    print("Não existe valor maior, os dois valores são IGUAIS.")