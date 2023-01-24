frase = str(input('Qual é a frase? ')).upper().replace(" ", "").strip()
fraseIN = frase[::-1]
if frase == fraseIN:
    print('é palindromo')
else:
    print('Não é palindromo')