# 47 - MOSTRAR NA TELA TOOOS OS NUMEROS PARES NO INTERVALO DE 1 ATÉ 50

print('-*-' * 5)
print('\033[32m EXERCICIO 50 \033[m')
print('-*-' * 5)
print()

print('INICIANDO CONTADOR')
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

print('FIM DO CONTADOR')