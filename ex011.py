#Calculo da quantidade de tinta necessária para pintar uma parede.
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg*alt
print ('Sua parede tem a dimensão de {}x{} e sua área é de {}m²')
ltinta = area/2
print('Você irá precisar de {}l de tinta'.format(ltinta))