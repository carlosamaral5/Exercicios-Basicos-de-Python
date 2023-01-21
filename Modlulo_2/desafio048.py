
soma=0
contador=0
for c in range(1,501,2):
    if c%3==0:
        soma=soma+c
        contador=contador+1

print('A soma de {} números múltiplos de 3 entre 1 e 500 é {}.'.format(contador,soma))    