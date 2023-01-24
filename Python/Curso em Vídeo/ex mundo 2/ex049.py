"""
n = int(input('digier um numero para ver sua tabuada: '))
a = 0

for c in range(1, 11):
    a += 1
    print('| {} x {:2} = {}'.format(n, a, n*a))
"""


n1 = int(input('Digite um valor: '))
for c in range(1, 11):
    print('|{} X {:2} = {}'.format(n1, c, n1*c))