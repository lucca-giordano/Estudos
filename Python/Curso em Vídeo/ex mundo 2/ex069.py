#region variaveis
idade = 0    # idade do cadastro atual
sexo = ' '   # sexo do cadastro atual
mais18 = 0   # quantas pessoas tem mais de 18
ht = 0       # quantos homens tem no total
m20m = 0     # quantas mulheres tem menos de 20
ctrl = ' '   # controle para continuar ou não
total = 0    #total de pessoas registradas
#endregion

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo [M/F]: '))
    ctrl = str(input('Quer continuar? [S/N]'))

    total += 1
    if idade >= 18:
        mais18 += 1
    if sexo in 'Mm':
        ht += 1
    if sexo in 'Ff' and idade < 20:
        m20m += 1
    if ctrl in 'Nn':
        break

print(f'''
Você registrou {total} pessoas no total, sendo elas:
{mais18} pessoas com mais de 18 anos
{ht} homens no total
{m20m} mulheres com menos de 20 anos
''')