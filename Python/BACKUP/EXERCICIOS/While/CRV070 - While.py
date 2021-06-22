# 070 - LER O PREÇO E VARIOS PRODUTOS E QUESTIONAR SE IRA CONTINUAR...
# TOTAL GASTO
# QUANTOS PRODUTOS CUSTAM MAIS DE 1000
# NOME DO PRODUTO MAIS BARATO

totmil = cnt = menorprc = total = 0
prodmb = ' '
while True:
    prod = str(input('Informe o produto: '))
    preço = float(input('Informe o preço do produto R$: '))
    cnt += 1
    total += preço

    # QUANTOS PRODUTOS CUSTAM MAIS DE 1000
    if preço > 1000:
        totmil += 1

    # NOME DO PRODUTO MAIS BARATO
    if cnt == 1 or preço < menorprc:
        menorprc = preço
        prodmb = prod

    flag = ' '
    while flag not in 'SN':
        flag = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if flag == 'N':
        break
print(f'O total gasto foi de R$ {total:.2f}')
print(f'{totmil} produtos custaram acima de R$1000.00')
print(f'O produto mais barato foi: {prodmb}')