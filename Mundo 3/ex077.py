'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('aprendizado', 'vontade', 'motivo', 'falta', 'sentimento', 'força', 'dia', 'imparavel', 'felicidade',
            'metas', 'projeto', 'vida')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
