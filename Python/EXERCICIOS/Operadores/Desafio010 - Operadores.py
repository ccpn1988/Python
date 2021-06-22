# CONVERSOR DE MOEDAS

from time import sleep
valor = float(input('Informe o valor disponivél em R$... '))
cotacao = float(4.88)
dolares = valor / cotacao

print('Efetuando a taxa cambial de USD par R$...')
sleep(1)

print(f'Você tem disponivel R$ {valor:.2f}, com isto vocÊ tem USD {dolares:.2f}')