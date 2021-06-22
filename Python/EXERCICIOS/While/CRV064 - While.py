# 064 - TRATANDO VARIOS VALORES V1.0
# LER VARIOS NUMEROS INTEIROS, PARA QUANDO FOR DIGITADO 999 E SOMAR TODOS DIGITADOS
# DESCONSIDERANDO 999

num = int(input('Digite um valor [STOP digite 999]:  '))
s = 0
cnt = 0
while num != 999:
    # ARMAZENANDO E SOMANDO OS NUMEROS DIGITADOS
    s += num
    num = int(input('Digite um valor [STOP digite 999]: '))
    # SOMANDO A QTD DE NUMEROS DIGITADOS
    cnt += 1
print('Acabou...')
print(f'Foram digitados {cnt} numeros, totalizando {s}')
