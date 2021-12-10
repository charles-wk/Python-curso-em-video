soma = 0
cont = 0
for c in range (0, 500, +3):
    if c%2 != 0:
        cont += 1
        soma += c
print ("SOMA DE TODOS OS {} NÚMEROS ÍMPARES MÚLTIPLOS DE TRÊS É {} ". format(cont, soma))