lista = ('arroz', 8.50, 
        'feijão', 5.50,
        'coquinha', 8.60,
        'guarana como refresca', 7.45)

n = -1   # gambiarra padrão
len = len(lista) - 1

while n < len:
    n += 1
    print(f'{lista[n]} custa ', end=' ')
    n += 1
    print(f'R${lista[n]}')
