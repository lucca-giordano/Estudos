#region variaveis
inp = True  # está no programa
step = 1    # paço do programa          1 = escolher numeros; 2 = escolher opção; 3 = mostrar resultado
num1 = 0    # primeiro numero
num2 = 0    # segundo numero
choice = 0  # opção escolhida
resp = 0    #resposta
#endregion

while inp == True:  # enquanto estiver dentro do jogo
    if step == 1:  #primeira etapa
        num1 = int(input('Escolha o primeiro numero: '))  # inserção do primeiro numero
        num2 = int(input('Escolha o segundo numero: '))  # inserção do segundo numero
        step = 2
    if step == 2:  #segunda etapa
        print('Escolha uma opção:\n\n[ 1 ] = soma\n[ 2 ] = multiplicar\n[ 3 ] = maior\n[ 4 ] = novos numeros\n[ 5 ] = sair do programa\n')  #pergunta a opção
        choice = str(input('Selecione uma opção: '))  #selecionar a opção
        step = 3  
    if step == 3:  #terceira etapa
        if choice == '1':  # caso escolha SOMAR
            resp = num1 + num2
            print('\nA soma de {} e {} é {}\n'.format(num1, num2, resp))
            step = 1

        elif choice == '2':  # caso escolha MULTIPLICAR
            resp = num1 * num2
            print('\nO produto de {} e {} é {}\n'.format(num1, num2, resp))
            step = 1

        elif choice == '3':  #caso escolha MAIOR
            if num1 > num2:
                print('\n{} é maior que {}\n'.format(num1, num2))
                step = 1
            elif num2 > num1:
                print('\n{} é maior que {}\n'.format(num2, num1))
                step = 1
            elif num1 == num2:
                print('\n{} é igual a {}\n'.format(num1, num2))
                step = 1

        elif choice == '4':  # caso escolha NOVOS NUMEROS
            step = 1

        elif choice == '5':  # caso escolha SAIR
            print('\nAdeus!')
            inp = False
        else:  # caso escolha alguma opção inexistente
            print('\nopção invalida, tente novamente\n')
            step = 2