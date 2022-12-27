
print(50*'&')
print('\033[1;34;43mNúmero Antecessor e Sucessor\033[m')
print(50*'&')

n=int(input('Digite um número: '))

a=n-1
s=n+1

print('O número digitado foi {} e seu antecessor é {} e o seu sucessor é {}'.format(n,a,s))