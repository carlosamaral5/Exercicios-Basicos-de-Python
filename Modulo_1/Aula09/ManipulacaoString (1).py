'''
01) frase='nbvg nbvff'
02) len('nbvg nbvff') => conta o número de caracteres;
03) frase.count(n) => conta quantas vezes o n aparece na frade;
04) frase.count(n,0,13) => conta quantas vezes o n aparece entre a posição 0 e a posição 12 (13-1)
05) frase.find('bvg') => vai dizer quantas vezes 'bvg' foi encontrado na frase. Se por acaso não existir essa string na frase será retornado o valor -1;
06) 'bvg' in frase => diz se a string existe na frase. Retorna o valor True ou False;
07) frase.replace('bvg','sua') => busca pela palavra 'bvg' e troca/substitui pela palavra 'sua';
08) frase.upper() => transforma todas as letras em maiúsculas;
09) frase.lower() => ao contrário de upper transforma todas as letras em minúsculas;
10) frase.captalize() => o primeiro caractere fica Maiúsculo e todos os outros minúsculos;
11) frase.title() => o primeiro caractere de cada palavra fica maiúsculo;
12) frase.strip() => remove todos os espaços desnecessários no início e no final da frase;
13) frase.rstrip() => revome todos os espaços a direita;
14) frase.lstrip => remove todos os espaços a esquerda;
15) frase.split() => divide a string considerando os espaços, ou seja, onde tem espaço é quebrada string e começa uma nova numeração, ou seja, divide a frase em uma lista de palavras;
16) '-'.join(frase) => faz a junção das palavras usando o separador '-' entre as palavras.
'''

frase='Curso em Video Python'

print(frase)
print(len(frase))
print(frase[9])
print(frase.count('C'))
print(frase.count('o',0,20))


