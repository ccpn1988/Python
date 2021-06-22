# FAÇA UM PROGRAMA QUE ESCOLHA UM NUMERO ALEATORIO ENTRE 0 E 5 E PEÇA PARA O USUÀRIO DESCOBRIR QUAL O NUMERO

from random import randint
from time import sleep

print('Pensando em um número entre 0 e 5...')
sleep(1) # TIMEOUT

# num = [1,2,3,4,5]
# escolha = random.choice(num)
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m'}

escolha = randint(0,5) # ESCOLHE DE FORMA ALEATÓRIA

n1 = int(input('Sua vez!! Qual número eu pensei? '))
print('PROCESSANDO...')

if n1 == escolha:
    print(f'VENCEU!!! O numero escolhido foi:{cores["azul"]} {escolha} {cores["limpa"]}  ')
else:
    print(f'PERDEU!!! O número escolhido foi:{cores["vermelho"]} {escolha} {cores["limpa"]}')