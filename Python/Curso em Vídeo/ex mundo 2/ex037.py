num = int(input('Insira um número: '))
met = str(input('Insira um método de conversão entre binário, octal e hexadecimal: [bin|oct|hex] '))

bina = bin(num)  #transforma em binario
octa = oct(num)  #trasnsforma em octal
hexa = hex(num)  #transforma em hexadecimal

print('-=-' * 48)
if met == 'bin' or met == '1':
    print('A conversão de {} para binario é: {}'.format(num, bina[2:]))
elif met == 'oct' or met == '2':
    print('A cnoversão de {} para octal é: {}'.format(num, octa[2:]))
elif met == 'hex' or met == '3':
    print('A conversão de {} para hexadecimal é: {}'.format(num, hexa[2:]))
else:
    print('Desculpe, parece que não encontrei nenhum método com o nome "{}"'.format(met))

