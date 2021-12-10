'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

d = 1
s = 0
c = 0
n = int(input("Digite um número: "))
p = input("Deseja continuar? [S/N] ").upper()
m = n
mn = n
while p != 'N':
    n1 = int(input("Digite um número: "))
    n2 = n1
    s = s + n2
    d += 1
    if n1 > n:
        m = n1
    else:
        mn = n1
    c += 1
    p = input("Deseja continuar? [S/N] ").upper()
media = (s+n)/d
print('O total de números digitados foi: {}'.format(c+1))
print("A media de numeros digitados foi: {}".format(media))
print("O maior número digitado foi: {}".format(m))
print("O menor número digitado foi: {}".format(mn))
