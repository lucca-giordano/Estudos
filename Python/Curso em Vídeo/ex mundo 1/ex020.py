from random import shuffle

nome1 = str(input('nome do primeiro grupo: '))
nome2 = str(input('nome do segundo grupo: '))
nome3 = str(input('nome do terceiro grupo: '))
nome4 = str(input('nome do quarto grupo: '))
cham = [nome1, nome2, nome3, nome4]
shuffle(cham)

print('A ordem dos grupos sorteada é:')
print(cham)