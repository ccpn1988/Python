# SOME DOIS NUMEROS E IMPRIMA EM TELA

from time import sleep

print('-=-' * 4)
print('DESAFIO003')
print('-=-' * 4)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print(f'Analisando os números digitados... ')
sleep(1)

print(f'A soma entre {n1} e {n2} é: {s}')