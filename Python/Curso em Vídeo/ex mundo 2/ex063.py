ant = int(input('Insira o numero: '))
prox = 1
som = 1
contr = int(input('Quantas vezes você gosstaria de receber o resultado? '))
while contr > 0:
    contr -= 1
    print(ant)
    som = prox + ant
    ant = prox
    prox = som

