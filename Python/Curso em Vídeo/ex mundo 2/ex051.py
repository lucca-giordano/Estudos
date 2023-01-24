pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dez = pri + (10 - 1) * raz

for c in range(pri, dez + raz, raz):
    print('{} '.format(c), end=' -> ')
print('FIM')