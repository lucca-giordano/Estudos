price = float(input('insira o valor do produto: R$'))
disc = (price / 100) * 5
newPrice = price - disc
print('O preço do produto é R${:.2f}. Com o disconto de 5%, o valor final será de R${:.2f}!!'.format(price, newPrice))