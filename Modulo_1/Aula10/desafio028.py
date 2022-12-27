
from random import randint

titulo='Advinhação'
print(10*'-*-')
print(titulo.center(30))
print(10*'-*-')

computador=randint(0,5)
jogador=int(input('Digite um número entre 0 e 5: '))

if computador == jogador:
    print('O número do computador foi {} e você ACERTOU!'.format(computador))
else:
    print('O número escolhido pelo computador foi {} diferente do seu número que foi {}. Tente outra vez!'.format(computador,jogador))
