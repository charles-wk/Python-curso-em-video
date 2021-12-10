'''Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem
de preços, organizando os dados em forma tabular.'''
print('-'*39)
print('          LISTAGEM DE PREÇOS')
print('-'*39)
listagem = ('Caderno', 12.00, 'Lápis de cor', 20.50, 'Borracha', 2.00, 'Cola', 3.50, 'Fichário', 32.90, 'Folhas', 10.90,
            'Livro', 34.90, 'Glitter', 0.50, 'EVA', 1.00, 'Tintas', 12.00, 'Cartolina', 0.75)
for c in listagem:
    if isinstance(c, str): #isinstance verifica o tipo da variavel
        print(f'{c: <12} ................. ', end='')
    else:
        print(f'  R${c: >4}')






