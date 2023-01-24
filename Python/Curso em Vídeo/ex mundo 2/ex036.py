prec = float(input('Insira o valor da casa: R$'))  #pergunta o preço da casa
sal = float(input('Insira seu salario: R$'))  #pergunta o salario
ans = float(input('Insira em quantos anos você quer pagar: '))  #pergunta em quantos meses será paga a casa

mes = ans * 12  #meses que serão pagas
mensal = prec / mes  #valor mensal
porc = (sal / 100) * 30  #porcentagem maxima

print('-=-'*48)
print('O valor da sua casa é de R${:.2f}, o seu salário é de R${:.2f}, e você quer pagar ela em {:.2f} meses.'.format(prec, sal, int(mes)))
if mensal > porc:
    print('O valor a ser pago por mes seria de R${:.2f}, porém com base no seu salário, o valor pago por mês não poderia exceder R${:.2f}\npor conta disso você \033[31mNÃO\033[m irá poder comprar a casa.'.format(mensal, porc))
elif porc > mensal:
    print('O valor a ser pago por mes sera de R${:.2f}, com base no seu salário, o valor pago por mes não poderia exceder R${:.2f}\npor conta disso você \033[32mPODE\033[m comprar sua casa'.format(mensal, porc))
