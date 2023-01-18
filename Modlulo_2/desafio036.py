
#Entradas

valor_imovel=float(input('Digite o valor do imóvel a ser financiado em R$: '))
soldo=float(input('Digite o valor do seu salário em R$:'))
ano=int(input('Digite a quantidade de anos que deseja financiar: '))

#Cálculos

parcela=valor_imovel/ano
if parcela < (0.30*soldo):
    print('Seu financiamento foi APROVADO e o valor da parcela é R$ {:.2f}.'.format(parcela))
else:
    print('Seu financiamento NÃO foi APROVADO. A parcela de R$ {:.2f} ultrapassou 30% do valor do seu salário.'.format(parcela))

print('Obrigado pela preferência!')