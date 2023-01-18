
#Entradas
num1 = int(input('Digite o PRIMEIRO valor: '))
num2 = int(input('Digite o SEGUNDO valor: '))

#Cálculos
if num1 > num2:
    print('O PRIMEIRO valor {} é maior que o SEGUNDO valor {}.'.format(num1, num2))
elif num2 > num1:
    print('O SEGUNDO valor {} é maior que o PRIMEIRO valor {}.'.format(num2, num1))
else:
    print('NÃO existe valor MAIOR. Os valores são iguais.')