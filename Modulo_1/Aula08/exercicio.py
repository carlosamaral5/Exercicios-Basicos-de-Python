import math
# from import math sqrt, floor => importa somente a funçao raíz quadrada e arredondamento para baixo
'''
IMPORTAÇÃO DE MÓDULOS
1) comando import e o nome do módulo importa todas as funcionalidades;
2) from comando import importa um funcionalidade específico;
3) import math => vai importar tudo
4) from math import sqrt => importa somente a funcionalidade raíz quadrada
4) math.ceil() => arredonda para cima
5) math.floor() => arredonda para baixo
6) randon.radint(1,10) => gera um aleatório inteiro entre 1 e 10
7) import random => gerar números aleatórios

'''

num=int(input('Digite um número: '))

raiz=math.sqrt(num)

print('A raiz quadrada do número {:.2f} é {:.2f}'.format(num,math.ceil(raiz)))
