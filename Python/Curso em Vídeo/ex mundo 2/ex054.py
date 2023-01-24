maior = 0
menor = 0
nacs = 0
for i in range(1, 8):
    nacs = int(input('Insira a {}° idade: '.format(i)))
    if nacs >= 18:
        maior += 1
    else:
        menor += 1
print('Menores de idade: {}'.format(menor))
print('Maiores de idade: {}'.format(maior))