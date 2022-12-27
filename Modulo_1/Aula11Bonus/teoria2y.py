#Cores nos programas

'''
Código ANSI => sempre começa com \033[código do estilo;código do texto;código de fundo m => \033[ ; ; m

Estilo
0 => None (estilo nenhum)
1 => Bold (em negrito)
4 => Underline (sublinhado)
7 => Negative (inverter configurações)

TEXTO
30 => Branco
31 => Vermelho
32 => Verde
33 => Amarela
34 => Azul
35 => Magenta
36 => Ciano
37 => Cinza

FUNDO
40 => Branco
41 => Vermelho
42 => Verde
43 => Amarela
44 => Azul
45 => Magenta
46 => Ciano
47 => Cinza

'''

nome='André Amaral'
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))