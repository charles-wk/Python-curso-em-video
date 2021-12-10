mulher = 0
media = 0
maior = 0

print("_"*30)
print("   INFORMAÇÕES DO GRUPO   ")
print("_"*30)
sexo = str(input("DIGITE SEU SEXO [M/F]: "))
sexo = sexo.upper()
nome = str(input("DIGITE SEU NOME: "))
idade = int(input("DIGITE SUA IDADE: "))
print("_"*30)

media += idade

if sexo == "M" and idade > 0:
    hvelho = nome
    maior = idade
elif sexo == "F" and idade < 20:
    mulher +=1

for cont in range(1, 3+1):
    sexo = str(input("DIGITE SEU SEXO [M/F]: "))
    sexo = sexo.upper()
    nome = str(input("DIGITE SEU NOME: "))
    idade = int(input("DIGITE SUA IDADE: "))
    print("_" * 30)

    media += idade

    if sexo == "M" and idade > maior:
            hvelho = nome
            maior = idade
    elif sexo == "F" and idade < 20:
        mulher += 1
#Verifica se há homens no "cadastro".
if maior == 0:
    print("   INFORMAÇÕES DO GRUPO   ")
    print ("_"*30)
    print ("MÉDIA DO GRUPO:{} ".format(media/4))
    print("MULHERES COM MENOS DE 20 ANOS: {}".format(mulher))
    print("_"*30)

else:
    print("   INFORMAÇÕES DO GRUPO   ")
    print("_" * 30)
    print("MÉDIA DO GRUPO: {}".format(media / 4))
    print("HOMEM MAIS VELHO: {}".format(hvelho))
    print("MULHERES COM MENOS DE 20 ANOS: {}".format(mulher))
    print("_" * 30)
