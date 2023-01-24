# nem eu sei o que eu fiz aqui
# funcionou e isso q importa

# Declaração de todas as variaveis

print('')
print('{:^40}'.format(' CASAS BAHIA '))
print('')

preco = float(input('Insira o valor da sua compra: R$'))  # pergunta o valor da compra
print('''
Métodos de pagamento:

[ car ] = cartão
[ din ] = dinheiro
[ che ] = cheque
 ''')
metodo = str(input('Insira o método de pagamento: ')).lower()  # pergunta o método de pagamento
vez = 1
if metodo == 'car':  # SE for cartão
    print('''Escolha em quantas vezes você irá pagar:
     
     a vista    = 5% de desconto
     2 vezes    = sem desconto
     3 ou mais  = 1% de juros por mês
     ''')
    vez = int(input('Em quantas vezes você gostaria de pagar? '))  # pergunta quantas vezes

print('-=-'*48)  # deixa bonitin
porc = preco / 100  # caucula UM porcento
parcela = preco / vez  # era pra mostrar quanto custa por mês


# aqui começa a treta
print('')

if metodo in 'din che':  # se o método for din o cheque
    porc = porc * 10
    preco = preco - porc
    print('Você irá pagar R${:.2f}, um total de 10% de desconto!'.format(preco))

elif metodo == 'car': # se o método for cartao blackzao tlgd ne paezao
    if vez <= 0:
        print('porra vai se fude tb né KKKKKKKKK')
    if vez == 1:  # se for em uma vez só
        porc = porc * 5
        preco = preco - porc
        print('Você irá pagar R${:.2f}, um total de 5% de desconto!'.format(preco))
    if vez == 2:  # se for em duas
        parcela = preco / vez
        print('Você irá pagar um total de R${:.2f} em 2 vezes juros, assim pagando R${:.2f} mensalmente.'.format(preco, parcela))
    if vez > 2:  # se for em 3 ou mais
        porc = porc * vez
        preco = preco + porc
        parcela = preco / vez
        print('Você irá pagar um total de R${:.2f}, em {} vezes com 1% de juros, assim pagando R${:.2f} mensalmente.'.format(preco, vez, parcela))

print('')