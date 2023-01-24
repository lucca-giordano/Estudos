num = 0
som = 0
total = 0
while num != 999:
    num = int(input('Insira um numero (999 para sair do programa): '))
    if num != 999:
        som += num
        total += 1
print('Voce digitou {} numeros, totalizando {}'.format(total, som))