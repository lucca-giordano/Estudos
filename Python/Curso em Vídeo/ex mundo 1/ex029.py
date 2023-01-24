velo = float(input('Insira sua velocidade: '))
maxi = 80
mul = velo - maxi
valor = 7
multa = mul * valor

if velo > maxi:
    print('Ah não! Você estava a {}km/h, o limite é somente {}km/h. Você pagara uma multa de R${:.2f}!'.format(velo, maxi, multa))
else:
    print('Relaxa, você estava a {}km/h, o limite é {}km/h, você não ira precisar pagar nenhuma multa'.format(velo, maxi))