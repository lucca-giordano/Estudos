#minha versão
'''
dia = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos quilometros você andou com o carro? '))
diaP = 60
kmP = 0.15
diaF = dia * diaP
kmF = km * kmP
total = diaF + kmF

print('O total da sua viagem ficou em:')
print('{} dias e {} quilometros.'.format(dia, km))
print('Assim totalizando R${:.2f}'.format(total))'''

#versão alternativa
diaALT = int(input('Quantos dias vc utilizou o carro? '))
kmALT = float(input('Quantos kilometros você andou com o carro? '))
pago = (diaALT * 60) + (kmALT * 0.15)
print('o total a pagar é de R${:.2f}'.format(pago))