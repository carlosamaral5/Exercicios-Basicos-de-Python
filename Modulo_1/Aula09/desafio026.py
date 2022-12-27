nom=str(input('Digite uma frase: ')).strip().upper().strip()

print('A letra A aparece {} vezes.'.format(nom.count('A')))

print('A primeira letra A aparece na posição {}.'.format(nom.find('A')+1))
print('A última letra A aparece na posição {}.'.format(nom.rfind('A')+1))