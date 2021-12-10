'''Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre elas (desconsiderando o flag). '''
s = t = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        print('Programa encerrado!')
        break
    n1 = n
    s += n1
    t += 1
print (f'Total de números digitados: {t}')
print(f'Soma de todos os números {s}')


