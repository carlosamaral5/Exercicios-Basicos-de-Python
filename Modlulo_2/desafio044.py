''' 1) à vista dinheiro/cheque: 10% de desconto
    2) à vista no cartão: 5% de desconto
    3) em até 2x no cartão: preço normal
    4) em 3x ou mais no cartão: 20% de juros
    '''
#Entradas
pn = float(input('Digite o preço do produto em R$ '))
print('{:=^40}'.format(' Lojas Amaral '))
print(''' Opções de pagamento:
[1] À vista em Dinheiro/Cheque
[2] À vista no Cartão
[3] Em até 2x no Cartão
[4] Em 3x ou mais no Cartão''')

op = int(input('Digite a opção de pagamento conforme a tabela acima: '))

#Cálculos

if  op == 1:
    total = pn*0.90
elif op == 2:
    total = pn*0.95
elif op == 3:
    total = pn
    parcela = total/2
    print('Sua compra será parcelada em 2x de R$ {:.2f}.'.format(parcela))
elif op == 4:
    total = pn*1.2
    qtdparc = int(input('Dividir em quantas parcelas? '))
    parcela = total/qtdparc
    print('Sua compra será parcelada em {}x de R$ {:.2f}.'.format(qtdparc,parcela))
else:
    print('Opção inválida! Favor escolher uma forma de pagamento válida.')
    
print('O valor das suas compras é R$ {:.2f} e, no final, custará um total de R$ {:.2f}'.format(pn,total))
   