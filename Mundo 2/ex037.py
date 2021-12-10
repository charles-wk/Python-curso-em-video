'''Um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
-1 para binário.
-2 para octal.
-3 para hexadecimal.'''

num = int(input('DIGITE UM NÚMERO: '))
print(30*"-")
print('''ESCOLHA A CONVERSÃO:
[1] CONVERSÃO PARA BINÁRIO
[2] CONVERSÃO PARA OCTAL
[3] CONVERSÃO PARA HEXADECIMAL''')
print(30*"-")

opcao = int(input("DIGITE SUA OPÇÃO: "))
print(30*"-")
if opcao == 1:
    print ("O NÚMERO {} EM BINÁRIO É: {}".format(num, bin(num)[2:]))

elif opcao== 2:
    print("O NÚMERO {} EM OCTAL É: {}".format(num, oct(num)[2:]))

elif opcao == 3:
    print ("O NÚMERO {} EM HEXADECIMAL É: {}".format(num, hex(num)[2:]))

else:
    print("OPÇÃO INVÁLIDA TENTE NOVAMENTE!")
print(30 * "-")