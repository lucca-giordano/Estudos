#minha versão
"""
import math
num = float(input('Digite um numero FLUTUANTE: '))
numTr = math.trunc(num)
print('seu numero é {}, e seu inteiro é {}.'.format(num, numTr))
"""
#versão alternativa

from math import trunc
num = float(input('Digite um numero FLUTUANTE: '))
print('Seu numero é {}, sua porção inteira é {}'.format(num, trunc(num)))

#versão alternativa

num = float(input('Digite um numero: '))
print('Seu numero é {}, sua porção inteira é {}'.format(num, int(num)))