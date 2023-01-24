num = []
newNum = 0
while True:
    newNum = int(input('Digite um numero [flag = -123]: '))
    if newNum == -123:
        break
    if newNum in num:
        print('Numero ja está na lista\n')
    else:
        num.append(newNum)
        print('Numero adcionado com sucesso\n')
num.sort() 
print(num)
