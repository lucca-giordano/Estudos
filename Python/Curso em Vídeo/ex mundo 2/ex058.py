from random import randint
pc = randint(0, 10)
pl = 11
tent = 0
print('O computador pensou em um número de 0 a 10, tente advinhar')
while pl != pc:
    pl = int(input('Qual numero você acha que é? '))
    tent += 1
    if pl > pc:
        print('Você errou. O computador pensou em um numero menor')
    if pl < pc:
        print('Você errou. O computador pensou em um numero maior')
print('Você acertou! Foram necessarias {} tentativas'.format(tent))