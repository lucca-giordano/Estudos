conta = str(input('Digite a expressão: '))
lista = []

for sim in conta:
    if sim == '(':
        lista.append('(')
    elif sim == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')