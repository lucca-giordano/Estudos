from random import randint
from time import sleep

pc = randint(0, 5)
print('-=-'*25)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar qual será...')
print('-=-'*25)
print('Processando...')
sleep(2)
pl = int(input('Qual numero eu pensei? '))
print('Processando...')
print('-=-'*25)
sleep(2)
if pl == pc:
    print('Parabens! Você acertou!')
else:
    print("""Você perdeu!
Eu pensei no número {}, e você disse {} """.format(pc, pl))
print('-=-'*25)
