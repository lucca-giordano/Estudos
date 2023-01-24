total = maismil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    prec = float(input('Valor do produto: R$'))
    cont += 1
    total += prec
    if prec >= 1000:
        maismil += 1
    if cont == 1 or prec < menor:
        menor = prec
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('----------FIM DO PROGRAMA----------')
print(f'''
Você comprou {cont} produtos, o valor total foi R${total:.2f}
Temos {maismil} produtos que custam mais de R$1000.00
{barato.capitalize()} é o produto mais barato, que custa R${menor:.2f}
''')