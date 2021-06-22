# 038 - COMPARANDO NUMEROS
# ESCREVA 2 NUMEROS E COMPARE-OS
# PRIMEIRO VALOR É MAIOR
# SEGUNDO VALOR É MAIOR
# NÃO EXISTE VALOR MAIOR AMBOS SÃO IGUAIS

from time import sleep
print('-=-' * 6)
print('\033[35mCOMPARANDO NUMEROS \033[m ')
print('-=-' * 6)

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'\033[31m O PRIMEIRO VALOR É MAIOR...\033[m')
elif num2 > num1:
    print(f'\033[32m O SEGUNDO VALOR É MAIOR...\033[m')
else:
    print(f'\033[34m NÃO EXISTE VALOR MAIOR, AMBOS SÃO IGUAIS\033[m')
