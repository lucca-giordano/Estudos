times = ('Fortaleza', 'Athletico-PR', 'Athletico-MG', 'Corinthians', 'Flamengo', 'Athletico-GO', 'Bragantino', 'Fluminense', 'Bahia', 'Palmeiras', 'Ceara', 'Santos', 'Internacional', 'Juventude', 'São paulo', 'Chapecoense', 'Cuiaba', 'Sport recife', 'Gremio', 'América')
print(f'5 primeiros colocados: {times[0:5]}\n')
print(f'4 ultimos colocados: {times[-4:]}\n')
print(f'Times em ordem alfabética: {sorted(times)}\n')
chapeco = times.index('Chapecoense') + 1
print(f'A chapecoense está em {chapeco}º posição.\n')
