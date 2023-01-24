pessoas = []
dados = []
maisP = []
menosP = []

while True:
    nome = str(input('Insira o nome: '))
    peso = int(input('Insira o peso: '))
    ctrl = str(input('Quer continuar? [s/n]: '))

    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()

    if ctrl in 'nN':
        break

for p in pessoas:
    if p[1] > 70:
        maisP.append(p[0])
    elif p[1] <= 70:
        menosP.append(p[0])

print(f'Pessoas mais pesadas: {maisP}')
print(f'Pessoas menos pesadas: {menosP}')