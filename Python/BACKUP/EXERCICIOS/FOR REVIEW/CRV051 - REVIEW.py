# 051 - PROGRESSÃO ARITMETICA
# LER O 1 TERMO E A RAZAO E MOSTRAR OS 10 PRIMEIROS TERMOS.

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
# DEFININDO O TERMO A SER EXECUTADO
termo10 = termo + (10 - 1) * razao

for i in range(termo, termo10 + razao, razao):
    print(f'{i} ', end='-> ')
print('ACABOU')