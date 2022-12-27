
print(50*'~')
print('\033[4;32;40mDobro, Tríplo e Raíz Quadrado\033[m')
print(50*'~')

n=int(input('Digite um número: '))

d=n*2
t=n*3
r=n**(1/2)

print('O número digitado foi {}, seu drobro é {}, seu triplo é {} e sua raíz quadrada é {:.2f}'.format(n,d,t,r))
