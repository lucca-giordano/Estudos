soma = 0
cont = 0
for c in range(1, 501):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados foram: {}'.format(cont, soma))