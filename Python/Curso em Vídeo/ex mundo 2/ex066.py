nun = 0
total = 0
soma = 0
while True:
    num = int(input('digite um numero [flag = 999]: '))
    if num == 999:
        break
    soma += num
    total += 1
print(f'\nVocê digitou {total} numeros')
print(f'A soma dos numeros digitados é {soma}\n')