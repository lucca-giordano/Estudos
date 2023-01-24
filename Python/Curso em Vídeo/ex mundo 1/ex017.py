#versão alternativa
"""
import math

co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente: '))
h = math.sqrt(co**2 + ca**2)

print('='*50)
print('Cateto oposto: {:.2f}'.format(co))
print('cateto adjacente: {:.2f}'.format(ca))
print('-'*50)
print('hipotenusa: {:.2f}'.format(h))
print('='*50)
"""
#versão alternativa
from math import hypot

co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente: '))
hi = hypot(co, ca)

print('Cateto oposto: {:.2f}'.format(co))
print('cateto adjacente: {:.2f}'.format(ca))
print('hipotenusa: {:.2f}'.format(hi))