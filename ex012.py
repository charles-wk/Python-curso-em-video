#Lê o preço de um produto e mostra seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço: '))
desconto = (5*preco)/100
print ('O valor com desconto de 5% será de: {}'.format(preco-desconto))
