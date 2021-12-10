''' Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.'''
print('Sequência Fibonacci')
c = int(input("Quantos termos você quer mostrar? "))
f = 1
f1 = f
r = 0
c1 = 3
print(0, f, f1, end=' ')
while c1 < c:
    c1 += 1
    r = f1 + f
    f1 = f
    f = r
    print(f, end=' ')
