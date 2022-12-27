
titulo='Início do programa'
print(50*'*')
print(titulo.center(50))
print(50*'*')

nome=str(input('Qual o seu nome? ')).strip()

if nome == 'André':
    print('O significado do seu nome é valente!')
else:
    print('Não sei o significado do seu nome.')
print('Fim')