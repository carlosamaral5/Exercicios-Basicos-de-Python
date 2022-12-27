
ano=int(input('Digite um ano qualquer: '))

print('Analisar se um ano é bissexto ou não.')

if (ano%4) == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
print('Fim do programa')