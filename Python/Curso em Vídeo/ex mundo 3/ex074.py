from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os numeros sorteados foram: {num[0]}, {num[1]}, {num[2]}, {num[3]}, {num[4]}\n')
print(f'O maior numero sorteado foi: {max(num)}')
print(f'O menor numero sorteado foi: {min(num)}\n')