lista = []
num = 0
five = False

while True:
    num=int(input('Insira um numero [flag = -123]: '))
    lista.append(num)
    if num == 5:
        five = True
    if num == -123:
        break

print(f'\nTarefa finalizada : lista = {lista}')

lista.sort(reverse=True)
print(f'''Foram digitados \033[34m{len(lista)}\033[m numeros
Lista em ordem decrescente: \033[34m{lista}\033[m
Numero 5 está na lista? \033[33m{five}\033[m
''')