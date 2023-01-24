peso = 0
maior = 0
menor = 0
for i in range(1, 6):
    peso = int(input('Insira o {}° peso: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('-=-'*10)
print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))
print('-=-'*10)