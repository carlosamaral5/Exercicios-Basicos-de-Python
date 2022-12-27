
branco='\033[1;30m'
vermelho='\033[1;31m'
verde='\033[1;32m'
amarelo='\033[1;33m'
azul='\033[1;34m'
magenta='\033[1;35m'
ciano='\033[1;36m'
cinza='\033[1;37m'
fecha='\033[m'

print(50*'+')
print(azul,'Cálculo Quantidade de Tinta',fecha)
print(50*'+')

l=float(input('Digite a largura em metros: '))
h=float(input('Digite a altura em metros: '))

a=l*h

qt=a/2

print('A área a ser pintada é de {}{:.2f}{} metros quadrados e vai precisar de {}{:.2f}{} litros de tinta'.format(verde,a,fecha,vermelho,qt,fecha))