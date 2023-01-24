nc = str(input('Nome completo: '))
ns = nc.split()

print('Muito prazer em te conhecer, {}!'.format(nc))
print('Primeiro nome: {}'.format(ns[0]))
print('Ultimo nome: {}'.format(ns[len(ns)-1]))