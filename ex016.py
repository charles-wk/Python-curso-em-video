#Ler o número e mostrar sua porção inteira
import math
num = float(input('Digite um número decimal: '))
print ('A porção inteira de {} é {}'.format(num, math.trunc(num)))