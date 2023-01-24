listaN = []
listaP = []
listaI = []

num = 0

while True:
    num = int(input('Insira um numero [flag = -123]: '))
    listaN.append(num)
    if num == -123:
        break
for i in listaN:
    if (i % 2 == 0):
        listaP.append(i)
    else:
        listaI.append(i)
if -123 in listaI:
    listaI.remove(-123)
    listaN.remove(-123)

print(f'A lista completa é: {sorted(listaN)}')
print(f'A lista dos pares é: {sorted(listaP)}')
print(f'A lista dos impares é: {sorted(listaI)}')