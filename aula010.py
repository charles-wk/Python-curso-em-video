'''nome = str(input('Qual é seu nome? '))
if nome == 'Charles':
    print ('Que nome lindo você tem!')
else:
    print('Seu nome é ok.')
    print('Bom dia, {}!'.format(nome))'''

n1 = float (input('Digite a primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print('A sua média foi: {:.1f}'.format(m))
print('Parabéns!' if m>= 6 else 'Estude mais!')
''''if m>= 6.0:
    print ('A sua média foi boa! Parabéns')
else:
    print('Sua média foi ruim!Estude mais!')'''