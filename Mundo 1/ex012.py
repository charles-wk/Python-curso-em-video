#Lê o preço de um produto e mostra seu novo preço, com 5% de desconto.
preço = float(input('Digite o preço: R$'))
desconto = preço - (5*preço/100)
print ('O valor de {:.2f} com desconto de 5% será de: R${:.2f}'.format(preço, desconto))
