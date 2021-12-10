'''Um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200KM
e R$0,45 para viagens mais longas.'''

km = float(input("Digite o a quantidade de quilômetros que irá viajar: "))
if (km <= 200):
    preco = km * 0.50
    print('O valor da passagem será de: R${:.2f}'.format(preco))
else:
    preco = km*0.45
    print('O valor da passagem será de: R${:.2f}'.format(preco))