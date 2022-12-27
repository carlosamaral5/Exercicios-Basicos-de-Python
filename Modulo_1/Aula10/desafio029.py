
vel=float(input('Digite a velocidade, em Km/h, do seu veículo agora: '))

if vel>80:
    print('Você ultrapassou o limite de velocidade de 80 km/h e pagará uma multa de {:.2f}.'.format(((vel-80)*7)))
else:
    print('Você está dentro do limite de velocidade. Faça uma ótima viagem!')
print('Tenha um bom dia! Dirija com segurança!')

