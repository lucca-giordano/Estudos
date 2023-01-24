n = int(input('Qual é sua idade? '))
tipo = 'n/a'

if n > 0 and n <= 9:
    tipo = 'mirim'
elif n > 9 and n <= 14:
    tipo = 'infantil'
elif n > 14 and n <= 19:
    tipo = 'junior'
elif n >= 20:
    tipo = 'master'
print('Você tem {} anos, logo você é do tipo {}'.format(n, tipo.upper()))