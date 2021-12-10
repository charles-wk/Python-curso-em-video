valor = list()
while True:
    valor.append(int(input('Digite um valor: ')))
    decisao = str(input('Deseja continua? [S/N]')).upper()
    if decisao in 'Nn':
        break
valor.sort(reverse=True)
print(f'Você digitou {len(valor)} elementos.')
print(f'Os valores em ordem decrecente são {valor}.')
if 5 in valor:
    print('O número 5 aparece na lista.')
else:
    print('O número 5 não aparece na lista.')
