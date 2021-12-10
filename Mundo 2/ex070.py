'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
t = mm = 0
p = str(input('Nome do produto: '))
v = int(input('Valor: R$'))
d = str(input('Continuar [S/N]: '))
t += v
v1 = mb = v
nmb = p
while True:
    p = str(input('Nome do produto: '))
    v = int(input('Valor: R$'))
    d = str(input('Continuar [S/N]: '))
    if v < v1 and v < mb:
        mb = v
        nmb = p
    if v > 1000:
        mm += 1
    t += v
    if d in 'nN':
        break
print(f'O total da compra foi R${t}.00')
print(f'{mm} produto(s) custando mais de R$1000.00')
print(f'Produto mais barato: {nmb} R${mb}')
