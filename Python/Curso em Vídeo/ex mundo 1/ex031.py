dist = int(input('Qual é a distancia da sua viagem? '))

if dist <= 200:
    print('O valor total será de R${}'.format(dist*0.5))
else:
    print('O valor será de R${}'.format(dist*0.45))