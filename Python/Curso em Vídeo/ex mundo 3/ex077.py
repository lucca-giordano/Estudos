palavras = ('no', 'feridos', 'atrair', 'convidar', 'supermercado', 'licor', 'hera', 'estrada', 'nascimento', 'mar')

for p in palavras:
    print(f'\nNa palavra \033[0;34m{p.upper()}\033[m temos: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(f'\033[0;33m{l.upper()}\033[m', end=', ')