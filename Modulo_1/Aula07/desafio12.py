
print(50*'=')
print('Cálculo de 5% sobre o Valor')
print(50*'=')




p=float(input('Digite o preço do produto desejado: '))

pp=p*0.95

print('O preço do produto é R$ \033[1;32m{:.2f}\033[m, mas com o desconto de 5% o seu preço promocional será de R$ \033[1;34m{:.2f}\033[m.'.format(p,pp))
