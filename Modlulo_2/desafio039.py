from datetime import date

#Entradas
nome = str(input('Digite seu PRIMEIRO nome: '))
ano_nasc = int(input('Digite o ANO do seu nascimento: '))
sexo = str(input('Digite "M" para o sexo MASCULINO e "F" para o sexo FEMININO:').lower())

#Cálculos
data_atual = date.today().year
idade = data_atual - ano_nasc
if sexo == 'm':
    if idade == 18:
        print('Quem nasceu em {}, tem {} anos e está no tempo de se alistar.'.format(ano_nasc,idade))
    elif idade < 18:
        print('Quem nasceu em {}, tem {} anos e falta {} anos para se alistar.'.format(ano_nasc, idade, 18 - idade))
    elif idade > 18:
        print('Quem nasceu em {}, tem {} anos e já passou {} anos do período de alistamento.'.format(ano_nasc, idade, idade - 18))
if sexo == 'f':
    print('Sexo FEMININO. Não há necessidade de alistamento.')

