# 046 - FAÇA UM PROGRAMA QUE EFETUE CONTAGEM REGRESSIVA PARA ESTOURO DE FOGOS
# INICIANDO EM 10 E TERMINANDO EM 0
# PAUSA DE 1S ENTRE ELES

from time import sleep

print('-=-' * 10)
print('\033[31m EXERCICIO 046 - LOOP FOR \033[m')
print('-=-' * 10)

for n in range(10, -1, -1):
    print(f'Contagem regressiva em: {n}')
    sleep(1)
print('\033[31m FOGOS !!!!!!!!!!!!! \033[m')