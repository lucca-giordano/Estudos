n = 0
while True:
    print('-='*20)
    n = int(input('Digite um numero para sua tabuada: '))
    if n <= 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')
print('\n-=-=-=-=-= PROGRAMA ENCERRADO -=-=-=-=-=\n')