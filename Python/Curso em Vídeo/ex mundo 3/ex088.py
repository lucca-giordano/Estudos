from random import randint

lista = []

for i in range(0, 6):
    gerador = [randint(1, 60), randint(1, 60),randint(1, 60),randint(1, 60),randint(1, 60),randint(1, 60)]
    lista.append(gerador)

print(f'''Primeira sugestão: {lista[0]}
Segunda sugestão: {lista[1]}
Terceira sugestão: {lista[2]}
Quarta sugestão: {lista[3]}
Quinta sugestão: {lista[4]}
Sexta sugestão: {lista[5]}''')