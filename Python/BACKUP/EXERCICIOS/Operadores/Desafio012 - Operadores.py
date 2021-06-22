# CALCULANDO DESCONTOS

from time import sleep

valor = float(input('Informe o valor a ser calculado.. '))
desc = float(valor * 5/100)
print('Calculando o desconto')
sleep(1)

print(f'O valor de descontos para R$ {valor:.2f} é de R$ {desc:.2f}, com isto o novo valor será R$ {valor - desc:.2f}')