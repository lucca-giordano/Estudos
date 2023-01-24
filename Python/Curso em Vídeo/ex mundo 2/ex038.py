num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

if num1 > num2:
    print('O primeiro número, {}, é maior que o segundo, {}.'.format(num1, num2))
elif num1 < num2:
    print('O segundo número, {}, é maior que o primeiro, {}.'.format(num2, num1))
else:
    print('Nenhum é maior que o outro, ambos são iguais. {} e {}.'.format(num1, num2))