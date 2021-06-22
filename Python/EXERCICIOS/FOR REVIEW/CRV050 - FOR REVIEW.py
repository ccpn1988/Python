# 050 - SOMANDO PARES
# LER 6 NUMEROS INTEIROS E SOMAR APENAS OS VALORES PARES
s = 0
cnt = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n}° numero:  '))
    if num % 2 == 0:
        # SOMANDO OS NUMEROS PARES
        s += num
        # SOMANDO A QTD DE NUMEROS PARES DIGITADOS
        cnt += 1
print(f'A soma dos {cnt} numeros pares digitados é {s}')