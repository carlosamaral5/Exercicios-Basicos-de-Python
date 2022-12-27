
branco='\033[1;30m'
vermelho='\033[1;31m'
verde='\033[1;32m'
amarelo='\033[1;33m'
azul='\033[1;34m'
magenta='\033[1;35m'
ciano='\033[1;36m'
cinza='\033[1;37m'
fecha='\033[m'


d=float(input('Digite o valor, em REAIS, que você tem na carteira: '))
tc=float(input('Digite o valor atual do DÓLAR: '))

vd=d/tc

print('Você tem R$ {}{:.2f}{} que equivale a quantida de US$ {}{:.2f}{}'.format(verde,d,fecha,vermelho,vd,fecha))
