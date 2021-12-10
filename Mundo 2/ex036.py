'''Programa para aprovar o empréstimo bancário para a compra de uma casa.
O pragrama vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.'''

valorCasa = float(input("Digite o valor da sua futura casa: R$"))
salario = float(input("Digite o valor do seu salário: R$ "))
ano = int(input("Digite a quantidade de anos que irá pagar: "))

valorParcela = valorCasa / (ano*12)

if valorParcela > (salario*30)/100:
    print("O valor da parcela excede 30% do seu salário, o empréstimo foi negado!")
else:
    print("Parabéns, você conseguiu o empréstimo! O valor da parcela será de {}x de {:.2f}!".format(ano*12, valorParcela))
