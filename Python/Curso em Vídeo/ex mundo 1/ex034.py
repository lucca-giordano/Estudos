sal = float(input('Qual é seu salario? R$'))
porc = sal / 100

if sal > 1250:
    print('Seu novo salario sera de R${:.2f}'.format(sal+porc*10))
if sal <= 1250:
    print('Seu novo salario será de R${:.2f}'.format(sal+porc*15))
