# 063 - FIBONACCI - TERMOS INICIADOS EM 0 - 1 OS PROXIMOS TERMOS E A SOMA DOS 2 ANTERIORES TERMO3 = 0 + 1
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos deve ser apresentado: '))
# TERMO 1 SEMPRE 0
t1 = 0
# TERMO 2 SEMPRE 1
t2 = 1
print('-' * 30)
print(f'{t1} -> {t2}',end='')
# INICIA O CONTADOR NO 3 TERMO, POIS T1 e T2 SÃO PADRÃO
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    # TRANSIÇÃO COM TERMOS (T1 e T2) SEMPRE IRÁ PROGREDIR, T2 PASSA A SER T3 e T1 PASSA A SER T2
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')