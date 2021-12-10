dsc = 0
p = int(input("DIGITE O PRIMEIRO VALOR: "))
s = int(input("DIGITE O SEGUNDO VALOR: "))
while dsc != 5:
    dsc = int(input((''' MENU
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMERO
    [5] SAIR DO PROGRAMA
 DIGITE O NÚMERO: ''')))
    print("==================================================")
    if dsc == 1:
        print ("SOMA")
        print (p+s)
        print("==================================================")
    elif dsc == 2:
        print("MULTIPLICAÇÃO")
        print (p*s)
        print("==================================================")
    elif dsc == 3:
        print("MAIOR")
        if p > s:
            print(p)
            print("==================================================")
        else:
            print(s)
            print("==================================================")
    elif dsc == 4:
        print("NOVOS NÚMEROS")
        p = (int(input("DIGITE O PRIMEIRO VALOR: ")))
        s = (int(input("DIGITE O SEGUNDO VALOR: ")))
        print("==================================================")



