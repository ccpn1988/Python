# 067 - TABUADA 3.0
# MOSTRARA TABUADA DE VARIOS NUMEROS, SENDO 1 POR VEZ E PARAR QUANDO O NUM SOLICITADO FOR NEGATIVO.

while True:
    n = int(input('Digite o numero para calcular a tabuada: '))
    print('-' * 40)
    if n < 0:
        break
    for tab in range(1,11):
        print(f'{n} x {tab} = {n * tab}')
    print('-' * 40)
print('Programa Tabuada encerrado')