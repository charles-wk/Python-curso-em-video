'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

p = 0
n = 0
t = 0
while p != 999:
    p = int(input("Digite um número [999 para parar]: "))
    n1 = p
    n = n + n1
    t += 1
print("A soma dos números digitados é de: {}".format(n-999))
print("O total de números digitados é de: {}".format(t-1))

'''Código do professor:
num = cont = soma = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    som += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: "))
ptint('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))'''
