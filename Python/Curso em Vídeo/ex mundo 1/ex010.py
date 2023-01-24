#minha versão
""""
mon = float(input('quanto dinheiro você tem na carteira? R$'))
dol = mon / 5.65
eu = mon / 6.78

print('Com R${}, você pode comprar US${:.2f}'.format(mon, dol))
print('Com R${}, você pode comprar €{:.2f}'.format(mon, eu))
"""

#versão alternativa
mon = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${}, você pode comprar US${:.2f}'.format(mon, mon/5.65))
print('Com R${}, você pode comprar €{:.2f}'.format(mon, mon/6.78))