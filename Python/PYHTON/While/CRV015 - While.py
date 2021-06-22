# INTERROMPENDO WHILE
# BREAK - PULA DO LAÇO
# CONTINUE = CONTI
n = s = qtd = 0
while True:
    n = int(input('Digite um número: '))
    # SE O NUMERO DIGITADO FOR 999, SAI DO LAÇO
    if n == 999:
        break
    qtd += 1
    s += n
print(f'Foram digitados {qtd} números e a soma dos números digitados é {s}')