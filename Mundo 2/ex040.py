'''Um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida'''

print("_"*30)
print("BEM VINDO - ANALISE A MEDIA")
print("_"*30)

n1 = float(input("DIGITE SUA PRIMEIRA NOTA: "))
n2 = float(input("DIGITE SUA SEGUNDA NOTA: "))
media = (n1+n2)/2

print("_"*30)

if media < 5:
    print ("RESULTADO DA MÉDIA: {:.1f}".format(media))
    print("REPROVADO")

elif media > 5 and media < 6.9:
    print("RESULTADO DA MÉDIA: {:.1f}".format(media))
    print("RECUPERAÇÃO")

else:
    print("RESULTADO DA MÉDIA: {:.1f}".format(media))
    print("APROVADO")