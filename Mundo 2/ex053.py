frase = str(input("Sua frase:"))
dividir = frase.split()
espaco = ''.join(dividir)
inverso = espaco[::-1]
print('O inverso de {} é {}'.format(espaco, inverso))
if inverso == espaco:
    print("É um palindromo!")
else:
    print("Não é um palindromo!")

'''Utilizando o for (código do professor)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto [letra]
if inverso == junt:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''
