# 065 - MAIOR E MENOR VALORES
# LER VARIOS NUMEROS
# MEDIA ENTRE OS NUMEROS DIGITADOS
# VALIDAR MAIOR E MENOR VALOR
# PERGUNTAR SE CONTINUA OU NÃO A DIGITAR VALORES

resp = 'S'
media = soma = qtd = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    # SEMPRE PARA VALIDAR MAIOR/MENOR O 1 LOOP O NUMERO SERA IGUAL MAIOR E MENOR
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    # MAIUSCULO, REMOVENDO ESPAÇOS, PEGANDO 1 LETRA
    resp = str(input('Quer continuar [S]/[N] ?')).upper().strip()[0]
media = soma / qtd
print(f'Você digitou {qtd} numeros e a média foi {media}')
print(f'O maior valor foi {maior} e o menor valor {menor}')
