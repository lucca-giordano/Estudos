a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = c
if a > b and a > c:
    maior = a
if b > c and b > a:
    maior = b


print('O menor numero é {}, e o maior é {}'.format(menor, maior))