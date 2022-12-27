'''
+ => adição
- => subtração
* => multiplicação
/ => divisão
** => potenciação
// => divisão inteira
% => resto da divisão
== => sinal de igualdade

ORDEM DE PRECEDÊNCIA
1º => ()
2º => **
3º => *, /, //, %
4º => +, -

DICAS
a) :.2f => significa que o número terá duas casas decimais
b) end='' => signifia que não quebrará a linha e o resultado será todo na mesma linha
c) \n => significa quebra de linha

'''
n1=int(input('Digite um número: '))
n2=int(input('Digite um número: '))

s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
p=n1**n2

print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s,m,d), end='')

print('A divisão inteira é {} e a potência é {}'.format(di,p))
