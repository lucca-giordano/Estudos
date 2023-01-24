from random import choice

nome1 = str(input('nome do primeiro aluno: '))
nome2 = str(input("nome do segundo aluno: "))
nome3 = str(input('nome do terceiro aluno: '))
nome4 = str(input('nome do quarto aluno: '))
cham = [nome1, nome2, nome3, nome4]
print('O aluno sorteado foi: {}'.format(choice(cham)))