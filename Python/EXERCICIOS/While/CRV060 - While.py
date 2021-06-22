# 060 - CALCULO FATORIAL
# from math import factorial
n = int(input('''Digite um numero para
calcular seu fatorial: '''))
# CONTADOR INICIALIZADO COM VALOR DIGITADO EM N
c = n
f = 1
print(f'Calculando {n}! = ',end='')
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ', end='')
    # FATORIAL RECEBENDO NUMERO DIGITADO
    f *= c
    # REMOVENDO VALOR DO CONTADOR
    c-= 1
print(f'{f}')



