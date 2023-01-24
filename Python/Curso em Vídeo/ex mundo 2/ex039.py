from datetime import date

nascimento = int(input('Em qual ano você nasceu? '))
idade = date.today().year - nascimento
alist = 18
falta = alist - idade
ja = idade - alist


if idade < alist:
    print('Ainda não está na hora de se alistar. Ainda faltam {} anos.'.format(falta))
elif idade > 18:
    print('Já passou da hora de se alistar, você deveria ter se alistado a {} anos atras.'.format(ja))
elif idade == 18:
    print('Está na hora de se alistar')