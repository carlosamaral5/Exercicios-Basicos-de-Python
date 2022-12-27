
'''
frase='curso em Vídeo Python'

print(frase)

print(frase[3:13])

print(frase[13:])

print(frase[1:20:2])

print(frase.count('o'))

print(frase.upper().count('o'))

print(len(frase))

frase=frase.replace('python','Android')
print(frase)

frase='Curso em Video Python'
frase=frase.replace('Python','Android')
print(frase)

print('Curso' in frase)
'''

frase='Curso em Vídeo Python'
dividido=frase.split()
print(dividido[0])
print(dividido[2][3])