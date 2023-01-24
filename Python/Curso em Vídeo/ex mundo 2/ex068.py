#region importações
from random import randint
#endregion

#region variaveis
pcjog = 0      # inicia jogada da maquina
pjn = 0        # numero do player
pjp = ' '      # escolha do player
par = True
#endregion

while True:
    pcjog = randint(0, 10)
    pjn = int(input('Digite um numero: '))
    pjp = str(input('Selecione PAR ou IMPAR [P/I]: '))
    
    if ((pcjog + pjn) % 2) == 0:
        par = True
    elif ((pcjog + pjn) % 2) != 0:
        par = False
    
    if pjp in 'Pp' and par == True:
        print('-=-=-=-=-Voce venceu!-=-=-=-=-\n')
        break
    if pjp in 'Pp' and par == False:
        print('Voce perdeu!\n')
    
    if pjp in 'Ii' and par == False:
        print('-=-=-=-=-Voce venceu!-=-=-=-=-\n')
        break
    if pjp in 'Ii' and par == True:
        print('Voce perdeu!\n')