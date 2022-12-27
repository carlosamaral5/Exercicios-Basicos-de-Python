
print(40*'*')
print('Analisador de Triângulo')
print(40*'*')

a = float(input('Digite o PRIMEIRO seguimento: '))
b = float(input('Digite o SEGUNDO seguimento: '))
c = float(input('Digite o TERCEIRO seguimento: '))

if a<b+c and b<a+c and c<b+a:
    print('É possível formar um TRIÂNGULO com as retas {:.2f}, {:.2f}, {:.2f}.'.format(
        a, b, c))
else:
    print('Não é possível formar um TRIÂNGULO com as retas {:.2f}, {:.2f}, {:.2f}.'.format(a, b, c))
