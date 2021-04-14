#Calculo da quantidade de tinta necessária para pintar uma parede.
alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = larg*alt
ltinta = area/2
print('Você irá precisar de {} latas de tinta'.format(ltinta))