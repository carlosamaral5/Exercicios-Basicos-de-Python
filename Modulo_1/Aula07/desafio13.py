
titulo = '\033[1;35;47m'
verde = '\033[1;32m'
azul = '\033[1;34m'
fecha = '\033[m'

print(50*'$')
print(titulo,'Cálculo Aumento de Salário',fecha)
print(50*'$')

s = float(input('Digite o valor do seu salário em R$: '))

sca = s*1.15

print('Seu salário é R$ {}{:.2f}{} e com um aumento de 15% ele passará ao valor de R$ {}{:.2f}{}.'.format(
    verde, s, fecha, azul, sca, fecha))
