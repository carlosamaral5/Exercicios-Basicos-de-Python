
dist=float(input('Digite a distância, em Km, da viagem a ser realizada: '))

if dist<=200:
    print('O valor da sua passagem é R$ {:.2f}.'.format(dist*0.50))
else:
    print('O valor da sua passagem é R$ {:.2f}.'.format(dist*0.45))
print('Obrigado pela preferência. Faça uma boa viagem!')