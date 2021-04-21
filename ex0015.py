#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
kmp = float(input('Seja bem vindo - Quantos KM você percorreu? '))
dia = int(input('Por quantos dias você alugou o carro? '))
pagar = (kmp*0.15) + (dia*60)
print ('O total a pagar é: R${:.2f}'.format(pagar))