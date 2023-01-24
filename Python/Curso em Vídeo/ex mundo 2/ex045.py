from random import randint
jog = str(input('Escolha entre pedra, papel ou tesoura: [ped|pap|tes] '))
pc = randint(1,3)

if jog == 'ped':  # se o player jogar pedra
    if pc == 1:
        print('a maquina jogou PEDRA e você PEDRA, foi um EMPATE')
    if pc == 2:
        print('a maquina jogou TESOURA e você PEDRA, VOCÊ GANHOU')
    if pc == 3:
        print('a maquina jogou PAPEL e você PEDRA, VOCÊ PERDEU')
if jog == 'pap':  # se o player jogar papel
    if pc == 1:
        print('a maquina jogou PEDRA e você PAPEL, VOCÊ GANHOU')
    if pc == 2:
        print('a maquina jogou TESOURA e você PAPEL, VOCÊ PERDEU')
    if pc == 3:
        print('a maquina jogou PAPEL, e você PAPEL foi um EMPATE')
if jog == 'tes':  # se o player jogar tesoura
    if pc == 1:
        print('a maquina jogou PEDRA e você TESOURA, VOCÊ PERDEU')
    if pc == 2:
        print('a maquina jogou TESOURA e você TESOURA, foi um EMPATE')
    if pc == 3:
        print('a maquina jogou PAPEL e você TESOURA, VOCÊ GANHOU')
