# 047 - CONTAGEM DE PARES
# TODOS OS NUMEROS PARES Q ESTAO NO INTERVALO ENTRE 1 E 50

for c in range(1, 51):
    if c % 2 == 0:
        print(f'{c}', end=' ')