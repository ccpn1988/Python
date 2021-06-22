# 066 - TRATANDO VARIOS VALORES V1.0
# LER VARIOS NUMEROS INTEIROS, PARA QUANDO FOR DIGITADO 999 E SOMAR TODOS DIGITADOS
# DESCONSIDERANDO 999

somar = qtd = 0

while True:
    n = int(input('Digite um numero: [Digite 999 para parar[: '))
    if n == 999:
        break
    somar += n
    qtd += 1
print(f'Foram digitados {qtd} numeros, com o total de {somar}')