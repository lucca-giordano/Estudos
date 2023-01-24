num = 0     # numero
quant = 0   # quantidade de numeros
total = 0   # soma total dos numeros
maior = 0   # maior numero
menor = 0   # menor numero
ctrl = 'Ss' # #controle de loop

while ctrl in 'Ss':
    num = int(input('Digite um numero: '))
    ctrl = str(input('Quer continuar? [S/N] '))
    quant += 1
    total += num
    if quant == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('A média é: {:.2f}'.format(total / quant))
print('O menor numero foi {} e o maior foi {}'.format(menor, maior))
