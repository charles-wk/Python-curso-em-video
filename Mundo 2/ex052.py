nprimo = 0

n = int(input("DIGITE UM NÚMERO INTEIRO: "))

for c in range (1, n+1):
    if n%c==0:
        nprimo+=1

if nprimo > 2:
    print("NÚMERO NÃO PRIMO")
else:
    print("NÚMERO PRIMO")