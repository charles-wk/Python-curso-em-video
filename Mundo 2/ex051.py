print("_"*30)
print("  10 TERMOS DE UMA PA  ")
print("_"*30)
p1 = int(input("PRIMEIRO TERMO: "))
r = int(input("RAZÃO: "))
d = p1 + (11-1) * r

for c in range(p1, d, r):
    print (c)

print("_"*30)