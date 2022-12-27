
nome=input('Digite o seu nome: ')

print('Nome com tdoas as letras maíusculas {}.'.format(nome.upper()))

print('Nome com todas a letras minúsculas {}.'.format(nome.lower()))

nse=nome.replace(' ','')
print('Número de letras sem considerar os espaços é {}.'.format(len(nse)))

dividido=nome.split()

print('O número de letras no primeiro nome é {}.'.format(len(dividido[0])))