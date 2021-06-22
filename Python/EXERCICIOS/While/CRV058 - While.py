# 058 - MELHORE O DESAFIO 28, COMPUTADOR PENSANDO UM NUMERO DE 0 a 10
# ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL A QTD DE PALPITES.

from random import randint
from time import sleep

print('Pensando em um número entre 0 e 10...')
sleep(1) # TIMEOUT

# num = [1,2,3,4,5]
# escolha = random.choice(num)
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}

escolha = randint(0,10) # ESCOLHE DE FORMA ALEATÓRIA
cnt = 0

n1 = int(input('Sua vez!! Qual número eu pensei? '))
print('PROCESSANDO...')

while n1 != escolha:
    cnt += 1
    n1 = int(input(f'Você erro {cnt} vezes. QUal numero eu pensei?  '))

if n1 == escolha:
    print(f'VENCEU!!! O numero escolhido foi:{cores["azul"]} {escolha} {cores["limpa"]} ', end=' ')
    print(f'Com {cnt} tentativas')
