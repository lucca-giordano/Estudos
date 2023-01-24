print('Gerador de PA')
print('-=-'*10)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
ter = pri
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(ter), end=' ')
        ter += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
print('FIM')
print('Progressão finalizada, com {} termos.'.format(total))