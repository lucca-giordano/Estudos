num = (int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: ')), int(input('Digite o terceiro numero: ')), int(input('Digite o quarto numero: ')))
nove = 0
tres = 0
for c in range(0, 4):
    if num[c] == 9:
        nove += 1
    if num[c] == 3:
        tres += 1

print(f'O numero 3 foi digitado {tres} vezes')
print(f'O numero 9 foi digitado {nove} vezes')
