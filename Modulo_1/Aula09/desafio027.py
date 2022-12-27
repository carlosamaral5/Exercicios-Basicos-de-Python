nom=str(input('Digite seu nome completo: ')).strip().title()

print(nom)

ns=nom.split()

#print(ns)

print('Seu primeiro nome é {}.'.format(ns[0]))
print('Seu último nome é {}.'.format(ns[len(ns)-1]))
