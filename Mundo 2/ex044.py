''''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
-À vista dinheiro cheque: 10% de desconto.
-À vista no cartão: 5% de desconto.
-Em até 2X no cartão: preço normal.
-3x ou mais no cartão: 20% de juros.'''

preco = float(input("DIGITE O VALOR DO SEU PRODUTO: R$ "))
print("-"*60)
print("LEIA ATENTAMENTE")
print("-"*60)
print("[1] À VISTA DINHEIRO/CHEQUE.")
print("[2] À VISTA NO CARTÃO.")
print("[3] 2 VEZES NO CARTÃO.")
print("[4] 3 VEZES NO CARTÃO [ESTA OPÇÃO ACRESCENTA 20% DE JUROS].")
print("[5] NÚMERO DE VEZES PERSONALIZADO [ESTA OPÇÃO ACRESCENTA 20% DE JUROS]. ")
print("[6] CANCELAR OPERAÇÃO")
condicao = int(input("DIGITE NÚMERO QUE REPRESENTA SUA FORMA DE PAGAMENTO:"))
print("-"*60)

if condicao == 1:
    preco = preco-(preco*10)/100
    print("PARABÉNS VOCÊ GANHOU 10% DE DESCONTO. O VALOR A PAGAR É: R${}".format(preco))

elif condicao == 2:
    preco = preco-(preco*5)/100
    print("PARABÉNS VOCÊ GANHOU 5% DE DESCONTO. O VALOR A PAGAR É: R${}".format(preco))

elif condicao == 3:
    preco = preco/2
    print("O VALOR A PAGAR É: 2X DE {}".format(preco))

elif condicao == 4:
    preco = (((preco*20)/100)+preco)/3
    print("O TOTAL É DE: R${}".format(preco * 3))
    print("ESTA CONDIÇÃO CONTÉM 20% DE JUROS. O VALOR A PAGAR É: 3X DE R${}".format(preco))

elif condicao == 5:
    excecao = int(input("DIGITE O NÚMERO DE VEZES [LIMITE MÁXIMO 10X]: "))
    preco = (((preco*20)/100)+preco)/excecao
    if excecao >= 0 and excecao <= 10:
        print("ESTA CONDIÇÃO CONTÉM 20% DE JUROS. O VALOR A PAGAR É: {}X DE R${}".format(excecao, preco))
    else:
        print("LIMITE FORA DO PADRÃO")
        print("FAVOR RECOMEÇAR!")
elif condicao == 6:
    print("OPERAÇÃO CANCELADA!")
print("-"*60)
print("OBRIGADO POR UTILIZAR O SISTEMA!")
print("-"*60)