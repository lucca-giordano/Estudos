s = ' '
while s not in 'MmFf':
    s = str(input('Digite seu sexo: [F/M]')).strip().upper()
    print('Dado invalido, digite novamente')
print('Sexo {}. Dado registrado com sucesso'.format(s))