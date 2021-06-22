# EXERCICIO 046 - CONTAGEM REGRESSIVA
# FAZER CONTAGEM REGRESSIVA DE 10 ATE 0 COM PAUSA DE 1 SEGUNDO ENTRE ELES.

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FOGOS !!!!')
