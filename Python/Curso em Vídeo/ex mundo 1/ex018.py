from math import sin, cos, tan, radians

an = float(input('Digite seu numero: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))

print('O seno de {} é {:.2f}'.format(an, sen))
print('O cosseno de {} é {:.2f}'.format(an, cos))
print('A tangente de {} é {:.2f}'.format(an, tan))