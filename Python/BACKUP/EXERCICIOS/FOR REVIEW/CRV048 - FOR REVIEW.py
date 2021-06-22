# 048 - SOMA IMPARES MULTIPLOS DE 3
# SOMAR TODOS NUMEROS IMPARES QUE SÃO MULTIPLOS DE 3 NO INTERVALO ENTRE 1 e 500

# ACUMULADOR
somar = 0
# CONTADOR
cnt = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        # ACUMULANDO OS VALORES DIVISIVEIS POR 3
        somar += i
        # CONTANDO A QTD DE NUMEROS DIVISIVEIS POR 3
        cnt += 1
        # MOSTRANDO OS NUMEROS DIVISIVEIS POR 3
        # print(f'{i}', end=' ')
print(f'A soma de todos os {cnt} números divisiveis por 3 é {somar}')
