lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',
'vinte e um', 'vinte e dois', 'vinte e três', 'vinte e quatro', 'vinte e cinco',
'vinte e seis', 'vinte e sete', 'vinte e oito', 'vinte e nove', 'trinta')

t = len(lista)
while True:
    num = int(input('\nSelecione um numero de 1 a 20 [flag = <0]: '))
    if num > 30:
        print('\n\033[0;31;40mNumero ainda não configurado\033[m')
    if num < 0:
        print('\nFlag acionado, \033[4;32;40msaindo do programa\033[m.')
        break
    if num in range(0, t):
        print(f'\nVocê selecionou \033[0;30;47m{lista[num].upper()}\033[m')