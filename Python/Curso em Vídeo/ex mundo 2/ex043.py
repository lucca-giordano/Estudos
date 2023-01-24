alt = float(input('Insira sua altura em cm: '))  #altura em centimetros
pes = float(input('Insira seu peso em kg: '))  #peso em kg
imc = pes / (alt/100)**2  #fórmula do IMC

if imc <= 18.5:
    print('Seu IMC é {:.1f}, isso é considerado magreza, obesidade grau 0.'.format(imc))
elif imc > 18.5 and imc <= 24.9:
    print('Seu IMC é {:.1f}, isso é considerado normal, obesidade grau 0.'.format(imc))
elif imc > 24.9 and imc <= 29.9:
    print('Seu IMC é {:.1f}, isso é considerado acima do peso, obesidade grau 1'.format(imc))
elif imc > 24.9 and imc <= 39.9:
    print('Seu IMC é {:.1f}, isso é considerado obeso, obesidade grau 2'.format(imc))
elif imc > 39.9:
    print('Seu imc é {:.1f}, isso é considerado gravemente obeso, obesidade grau 3.'.format(imc))