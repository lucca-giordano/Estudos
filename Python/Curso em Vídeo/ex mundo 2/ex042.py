a = float(input('Primeiro lado: '))  #primeiro lado
b = float(input('Segundo lado: '))  #segundo lado
c = float(input('Terceiro lado: '))  #terceiro lado
pod = False  #se ele pode formar ou não, false por padrão

if a < b + c and b < a + c and c < a + b: #caucula se pode se formar um triangulo
    pod = True
    print('Os lados acima podem se tornar um triângulo: ')
else:  #caso não seja possivel
    pod = False
    print('Os lados acima não podem formar um triângulo')

if pod == True:  #faz ps bang pra decidir qual tipo de triangulo é
    if a == b == c:
        print('O triangulo é equilatero, todos os lados são iguais')
    elif a != b != c != a:
        print('O triangulo é escaleno, todos os lados são diferentes')
    else:
        print('O triangulo é isóceles, somente 2 lados são iguais')
elif pod == False:  #a vai toma no cukkkk
    print('a vai toma no cukkkk')