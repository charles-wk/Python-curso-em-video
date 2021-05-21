'''Crie um programa que fale se o nome da cidade começa ou não com "Santo"'''

cidade = str(input('Digite o nome de sua cidade: '))
cidade = cidade.upper().split()
print ('Sua cidade começa com Santo? ')
print('SANTO' in cidade[0])