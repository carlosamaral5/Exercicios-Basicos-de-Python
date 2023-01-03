
#Entradas
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))

#Cálculo
imc = peso/pow(altura,2)

#Saídas
if imc < 18.5:
    print('Seu imc é {:.2f} e, portanto, você está ABAIXO DO PESO.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu imc é {:.2f} e, portanto, você está com o PESO IDEAL.'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu imc é {:.2f} e, portanto, você está com SOBREPESO.'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu imc é {:.2f} e, portanto, você está com OBESIDADE.'.format(imc))
else:
    print('Seu imc é {:.2f} e, portanto, você está com OBESIDADE MÓRBIDA.'.format(imc))