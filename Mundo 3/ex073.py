campeonato = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Internacional', 'Corinthians',
              'Fluminense', 'Atlético-GO', 'América-MG', 'Cuiabá', 'Athletico-PR', 'São Paulo', 'Ceará', 'Bahia',
              'Santos', 'Juventude', 'Sport', 'Grêmio', 'Chapecoense')
print('-'*60)
print(f'TIMES DO BRASILEIRÃO: {campeonato}')
print('-'*60)
print(f'5 PRIMEIROS COLOCADOS: {campeonato[0:5]}')
print('-'*60)
print(f'4 ÚLTIMOS COLOCADOS: {campeonato[-4:]}')
print('-'*60)
print(f'ORDEM ALFABÉTICA: {sorted(campeonato)}')
print('-'*60)
print(f'Chapecoense está na {campeonato.index("Chapecoense")+1}ª posição')
print('-'*60)
