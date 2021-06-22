# 045 - JOKEMPO
from time import sleep
from random import randint

print('EXERCICIO 045 - JOKENPO')

# DEFININDO OS ITENS E AUTOMATIZANDO A ESCOLHA DO COMPUTADOR
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

# DEFININDO A OPÇÂO DE ESCOLHAS DO JOGADOR
print('''Escolha sua opção: 
[ 0 ] - PEDRA 
[ 1 ] - PAPEL
[ 2 ] - TESOURA ''')

jogador = int(input('Qual é a sua jogada? '))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-' * 9)
print(f'Computador jogou: \033[31m{itens[computador]}\033[m ')
print(f'Jogador jogou: \033[32m{itens[jogador]}\033[m ')
print('-=-' * 9)

if computador == 0:
    if jogador == 0:
        print('\033[33m EMPATE \033[m')
    elif jogador == 1:
        print('\033[32m JOGADOR VENCE \033[m')
    elif jogador == 2:
        print('\033[31m COMPUTADOR VENCE \033[m')
    else:
        print('\033[34m JOGADA INVALIDA \033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[31m COMPUTADOR VENCE \033[m')
    elif jogador == 1:
        print('\033[33m EMPATE \033[m')
    elif jogador == 2:
        print('\033[32m JOGADOR VENCE \033[m')
    else:
        print('\033[34m JOGADA INVALIDA \033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[32m JOGADOR VENCE \033[m')
    elif jogador == 1:
        print('\033[31m COMPUTADOR VENCE \033[m')
    elif jogador == 2:
        print('\033[33m EMPATE \033[m')
    else:
        print('\033[34m JOGADA INVALIDA \033[m')
