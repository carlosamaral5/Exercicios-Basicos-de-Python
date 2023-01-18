
print(40*'*')
print('Analisador de Triângulo')
print(40*'*')

#Entradas
a = float(input('Digite o PRIMEIRO seguimento: '))
b = float(input('Digite o SEGUNDO seguimento: '))
c = float(input('Digite o TERCEIRO seguimento: '))

#Cálculos
#Dá pra formar um TRIÂNGULO?
if a<b+c and b<a+c and c<b+a:
    print('É possível formar um TRIÂNGULO com as retas {:.2f}, {:.2f}, {:.2f}.'.format(
        a, b, c))
else:
    print('Não é possível formar um TRIÂNGULO com as retas {:.2f}, {:.2f}, {:.2f}.'.format(a, b, c))

#Qual o tipo de TRIÂNGULO?
if a == b and b == c:
    print('Todos os lados do triângulo são iguais e, portanto é um triângulo EQUILÁTERO.')
elif a == b or b == c or c == a:
    print('O triângulo tem dois lados iguais e, portnato é um triângulo ISÓCELES.')
else:
    print('Todos os lados são diferentes e, portanto é um triângulo ESCALENO.')