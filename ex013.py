#Adicionar 15% de aumento no salário do funcionário
salario = float(input('Digite seu salário: R$'))
aumento = salario + (salario*15/100)
print ('Seu novo salário com aumento de 15% será de: R${:.2f}'.format(aumento))