valor = list()
valor1 = (int(input('Digite um valor para posição 0: ')))
maior = valor1
posicaomaior = 0
posicaomaior2 = 0
menor = valor1
posicaomenor = 0
posicaomenor2 = 0

#arruarindice
for indice in range(0,4):
    valor.append(int(input(f'Digite um valor para posição {indice+1}: ')))
    if valor[indice] > maior:
        maior = valor[indice]
        posicaomaior = indice+1
        if valor[indice]==maior:
            posicaomaior2 = indice+1
    elif valor[indice] < menor:
        menor = valor[indice]
        posicaomenor = indice+1
        if valor[indice]==maior:
            posicaomenor2 = indice+1

print(f'O maior valor digitado foi {maior}, na posições {posicaomaior}.. {posicaomaior2}..')
print(f'O menor valor digitado foi {menor}, na posições {posicaomenor}.. {posicaomenor2}..')
