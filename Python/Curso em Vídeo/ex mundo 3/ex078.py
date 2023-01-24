num = []

print('\n')

for v in range(1, 6):
    num.append(int(input(f'Insira o {v}º numero: ')))

maxV = max(num)
maxI = num.index(maxV)

minV = min(num)
minI = num.index(minV)


print(f'Você digitou os valores: {num}\n')
print(f'O maior valor digitado foi {maxV}, na posição {maxI}')
print(f'O menor valor digitado foi {minV}, na posição {minI}\n')