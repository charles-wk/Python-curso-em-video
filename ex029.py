'''Um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada KM acima do limite'''

vel = float(input('Escreva a velocidade do carro, Km/H: '))

if vel > 80:
    multa = (vel-80) * 7.00
    print('Você foi MULTADO por excesso de velocidade! Diriga com cuidado!')
    print('O valor da multa a pagar é de: R$ {:.2f}'.format(multa))

print('Você está dentro do limite de velocidade! Dirija com cuidado')