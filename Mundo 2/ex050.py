soma=0
cont=0
print("_"*30)
print("        SOMA DE PARES")
print("_"*30)
for c in range (0,6):
    n = int(input("NÚMERO INTEIRO: "))
    if n%2==0:
        soma += n
        cont += 1
print("_"*30)
print("TOTAL Nº PARES: {}".format(cont))
print("RESULTADO: {}".format(soma))
print("_"*30)