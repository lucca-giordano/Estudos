# maneira numerica

num = int(input('Insira um numero de 0 a 99999: '))
uN = num // 1 % 10
dN = num // 10 % 10
cN = num // 100 % 10
mN = num // 1000 % 10
dmN = num // 10000 % 10

print('='*50)
print('Unidade: {:10}'.format(uN))
print('Dezena: {:11}'.format(dN))
print('Centena: {:10}'.format(cN))
print('Milhar: {:11}'.format(mN))
print('Dezena de milhar: {}'.format(dmN))
print('='*50)

# trabalhar a str
# da problema essa porra, nem tenta

numS = str(num)
print('Unidade: {:10}'.format(numS[3]))
print('Dezena: {:11}'.format(numS[2]))
print('Centena: {:10}'.format(numS[1]))
print('Milhar: {:11}'.format(numS[0]))
print('='*50)
