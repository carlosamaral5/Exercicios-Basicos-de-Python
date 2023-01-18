import datetime

#Entradas
nome = str(input('Digite seu nome: '))
ano_nasc = int(input('Digite o ano de seu nascimento: '))

#Cálculos
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc


if idade <= 9:
    print('{} você tem {} anos e está na categoria MIRIM.'.format(nome, idade))
elif idade > 9 and idade <= 14:
    print('{} você tem {} anos e está na categoria INFANTIL.'.format(nome, idade))
elif idade > 14 and idade <= 19:
    print('{} você tem {} anos e está na categoria JÚNIOR.'.format(nome, idade))
elif idade > 19 and idade <= 20:
    print('{} você tem {} naos e está na categoria SÊNIOR.'.format(nome, idade))
else:
    print('{} você tem {} anos e está na categoria MÁSTER.'.format(nome, idade))
