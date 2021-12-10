'''Um programa que leia três números
e mostre qual é o maior e qual é o menor.'''

n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite um segundo número qualquer: '))
n3 = int(input('Digite um terceiro número qualquer: '))
#verifica quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#verificar quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print ('O menor número digitado foi: {}'.format(menor))
print ('O maior número digitado foi: {}'.format(maior))