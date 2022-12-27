
a=float(input('Digite o PRIMEIRO número: '))
b=float(input('Digite o SEGUNDO número: '))
c=float(input('Digite o TERCEIRO número: '))

#Verificar o MENOR
menor=a
if b<a and b<c:
    menor=b
if c<a and c<a:
    menor=c

# Verificar o MAIOR
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c

print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))


