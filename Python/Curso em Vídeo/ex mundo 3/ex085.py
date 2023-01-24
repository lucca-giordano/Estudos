lista = []
impar = []
par = []

for i in range(0, 7):
    num = int(input('Insira um numero: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

par.sort()
impar.sort()

lista.append(impar)
lista.append(par)

print(lista)