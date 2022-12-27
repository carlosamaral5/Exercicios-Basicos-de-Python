
titulo='Iniciando Programa'
print(50*'*')
print(titulo.center(50))
print(50*'*')

n1=float(input('Digite a PRIMEIRA nota: '))
n2=float(input('Digite a SEGUNDA nota: '))

m=(n1+n2)/2

if m>=5.0:
    print('Sua média foi {:.2f} e, portanto, você foi APROVADO!'.format(m))
else:
    print('Sua média foi {:.2f} e, portanto, você foi REPROVADO!')

