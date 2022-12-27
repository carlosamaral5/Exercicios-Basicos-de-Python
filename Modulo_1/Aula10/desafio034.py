
sal=float(input('Digite seu salário em R$: '))

if sal>1250:
    aum=sal*1.10
else:
    aum=sal*1.15
print('Seu salário é R$ {:.2f} e com o aumento ficará R$ {:.2f}.'.format(sal,aum))
