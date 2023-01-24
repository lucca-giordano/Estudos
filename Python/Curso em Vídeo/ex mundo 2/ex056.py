"""
    Desenvolva um programa que leia o NOME, a IDADE e o SEXO de 4 pessoas, e no final mostre:
    - a média de idade DO GRUPO
    - o nome do HOMEM MAIS VELHO
    - quantas MULHERES MENORES QUE 20
"""

#region variaveis necessarias
nome = ''  #nome
sexo = ''  #sexo
idade = 0  #idade
nomeV = '' #nome do homem mais velho
idadeMaior = 0 #idade do homem mais velho
totM = 0   #total de mulheres menores de 20 anos
idadeTotal = 0 #soma total das idades
idadeM = 0 #media das idades
#endregion

# gloria a deus pai do céu amem q isso funcionou eu ja tava ficando louco ja


for i in range(1, 5):
    print('------ Pessoa n° {} ------'.format(i))
    nome = str(input('Insira o nome: '))
    sexo = str(input('Selecione o sexo: [F/M] '))
    idade = int(input('Insira a idade: '))
    print('-------------------------')
    idadeTotal += idade
    idadeM = idadeTotal / 4
    
    if sexo in 'Ff' and idade < 20:
        totM += 1
    if i == 1 and sexo in 'Mm':
        nomeV = nome
        idadeMaior = idade
    if sexo in 'Mm' and idade > idadeMaior:
        idadeMaior = idade
        nomeV = nome
 
#imprime os valores
print('A média de idades é {:.1f}'.format(idadeM))

if totM == 1:
    print('{} mulher tem menos de 20 anos'.format(totM))
elif totM > 1:
    print('{} mulheres tem menos de 20 anos'.format(totM))

if nomeV == '':
    print('Não detectamos nenhum homem no sistema')
else:
    print('{} é o nome do homem mais velho, com {} anos'.format(nomeV, idadeMaior))