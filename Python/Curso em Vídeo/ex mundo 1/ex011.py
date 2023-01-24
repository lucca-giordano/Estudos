#minha versão
"""
alt = float(input('altura da parede: '))
larg = float(input('largura da parede: '))
res = alt * larg
tint = res / 2

print('a altura da sua parede é {}, a largura da sua parede é {}. '.format(alt, larg))
print('a area total da sua parede é {}m²'.format(res))
print('Você ira precisar de um total de {}L de tinta para pintar toda a parede.'.format(tint))
"""

#versão alternativa

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
print('A altura da sua parede é de {}'.format(altura))
print('A largura da sua parede é de {}'.format(largura))
print('A área total da sua parede é de {:.2f}m²'.format(altura*largura))
print('A quantidade de tinta necessaria para pintar a parede será de {:.2f}L'.format((altura*largura/2)))