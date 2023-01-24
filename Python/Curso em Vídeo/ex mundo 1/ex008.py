#minha versão
"""
m = int(input('numero em metros: '))
km = m / 1000
cm = m * 100
mm = cm * 100

print('o valor em QUILOMETROS é: {}'.format(km))
print('O valor em METROS é: {}'.format(m))
print('O valor em CENTIMETROS é: {}'.format(cm))
print('O valor em MILIMETROS é: {}'.format(mm))
"""
#versão alternativa

m = int(input('numero em metros: '))
print('O valor em QUILOMETROS é: {}'.format((m/1000)))
print('O valor em METROS é: {}'.format(m))
print('O valor em CENTIMETROS é: {}'.format((m*100)))
print('O valor em MILIMETROS é: {}'.format((m*10000)))