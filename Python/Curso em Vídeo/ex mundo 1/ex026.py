fr = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes.'.format(fr.count('A')))
print('A primeira letra A aparece em {}'.format(fr.find('A')+1))
print('A ultima letra A aparece em {}'.format(fr.rfind('A')+1))
