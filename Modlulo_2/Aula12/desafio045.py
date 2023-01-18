from random import randint
from time import sleep
#Entradas
opçoes=('Pedra','Papel','Tesoura')
computador = randint(0,2)

print('{:#^40}'.format(' Jogo JoKenPo '))
print('''Escolha uma das opções abaixo:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador=int(input('Digite uma das opções acima: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('%'*30)
print('Computador escolheu: {}'.format(opçoes[computador]))
print('Você escolheu: {}'.format(opçoes[jogador]))
print('%'*30)

#Cálculos
if computador == 0: #computador escolhe PEDRA
    if jogador == 0:
        print('Jogo EMPATADO! Ambos escolheram PEDRA.')
    elif jogador == 1:
        print('Parabéns! Você GANHOU!')
    elif jogador == 2:
        print('O  computador GANHOU!')    
    else:
        print('Jogada INVÁLIDA. Tente novamente!')
   
elif computador == 1: # O computador escolheu PAPEL
    if jogador == 0:
        print('O computador GANHOU!')
    elif jogador == 1:
        print('Jogo EMPATADO! Ambos escolheram PAPEL!')
    elif jogador == 2:
        print('Parabéns! Você GANHOU!')    
    else:
        print('Jogada INVÁLIDA. Tente novamente!')
elif computador == 2: # O computador escolheu TESOURA
    if jogador == 0:
        print('Parabéns! Você GANHOU!')
    elif jogador == 1:
        print('O computador GANHOU!')
    elif jogador == 2:
        print('Jogo EMPATADO. Ambos escolheram TESOURA!')    
    else:
        print('Jogada INVÁLIDA. Tente novamente!')
else:
    print('Escolha uma opção válida.')
