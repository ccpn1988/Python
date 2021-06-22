# CRIAR UM PROGRAMA QUE LEIA UM NUMERO E MOSTRE SE ELE È PAR OU IMPAR

from time import sleep

num = int(input('Digite um número: '))
print('Verificando o número digitado')

if num % 2 > 0:
    print(f'O numero digitado é {num} ele é IMPAR')
else:
    print(f'Você digitou o numero {num} ele é PAR!!!')
