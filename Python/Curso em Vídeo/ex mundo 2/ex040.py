num1 = float(input('Insira a primeira nota: '))  #primeira nota
num2 = float(input('Insira a segunda nota: '))  #segunda nota
med = (num1 + num2) / 2  #caucula a media

if med < 5:
    print('Sua média é de {} Você está foi reprovado.'.format(med))
elif med >= 5 and med < 7:
    print('Sua média é de {} Você está de recuperação.'.format(med))
elif med >= 7 and med <= 10:
    print('Sua média é de {} Você está aprovado'.format(med))
elif med > 10:
    print('sai daq essa nota n existe n zé KKKKKK')

