a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    print('Os lados acima podem se tornar um triângulo: ')
else:
    print('Os lados acima não podem formar um triângulo')
    