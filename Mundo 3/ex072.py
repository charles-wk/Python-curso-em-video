extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = 'S'
while continuar in 'S':
    numero = int(input('Digite um número de 0 a 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('Tente novamente. Digite um número de 0 a 20: '))
    if numero > 0 or numero < 20:
        print(f'Você digitou o número {extenso[numero]}.')
    continuar = (str(input('Quer continuar? [S/N]'))).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = (str(input('Tente Novamente. Quer continuar? [S/N]'))).upper()





