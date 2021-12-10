while True:
    n = int(input('Qual tabuada deseja mostrar? '))
    if n < 0:
        print('Programa encerrado!')
        break
    for c in range(1,11):
        t = n*c
        print(f'{n} x {c} = {t}')
