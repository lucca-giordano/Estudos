ctrl = ' '
saque = total = resto = ced50 = ced20 = ced10 = moed1 = 0

while True:
    saque = int(input('Digite o valor a sacar: '))
    total += saque

    ced50 = total // 50
    resto = total % 50

    ced20 = resto // 20
    resto = resto % 20

    ced10 = resto // 10
    resto = resto % 10

    moed1 = resto

    print(f'\nO valor total sacado foi de R${total:.2f}\nvocê irá precisar de:\n')
    if ced50 > 0:
        print(f'{ced50} cédulas de R$50')
    if ced20 > 0:
        print(f'{ced20} cédulas de R$20')
    if ced10 > 0:
        print(f'{ced10} cédulas de R$10')
    if moed1 > 0:
        print(f'{moed1} moedas de R$1')

    total = 0
    ctrl = str(input('Quer fazer mais um saque? [S/N] ')).strip().upper()[0]
    if ctrl == 'N':
        break