
#Entradas
num=int(input('Digite um número qualquer: '))

#Cálculos
bina = bin(num)
octa = oct(num)
hexa = hex(num)

#Saídas
print('O número digita foi {}.'.format(num))
print('Tranformado em binário fica {}.'.format(bina[2::]))
print('Transformado em cotadecimal fica {}.'.format(octa[2::]))
print('Transformado em hexadecimal fica {}.'.format(hexa[2::]))

