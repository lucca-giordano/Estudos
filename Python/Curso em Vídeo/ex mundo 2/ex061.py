print('Gerador de PA')
print('-=-'*10)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
ter = pri
cont = 1

while cont <= 10:
    print('{} -> '.format(ter), end=' ')
    ter += raz
    cont += 1
print('FIM')

