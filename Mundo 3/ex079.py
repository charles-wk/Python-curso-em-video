valores = list()
valores.append(int(input(f'Digite um valor para posição 0:')))
conferir = valores
print('Número adicionado com sucesso!')
for p, indice in enumerate(range(0, 4)):
    valores.append(int(input(f'Digite um valor para posição{p}:')))
    if conferir in valores:
        print('Número cancelado! Já está na lista')
    else:
        print('Número adicionado com sucesso!')
    conferir = valores[indice]
