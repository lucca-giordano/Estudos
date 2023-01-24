sal = float(input('insira seu salario: R$'))
aum = (sal / 100) * 15
fin = sal + aum

print('Seu salário atual é de R${}, com o aumento de 15% ele passará a ser de R${:.2f}!!'.format(sal, fin))