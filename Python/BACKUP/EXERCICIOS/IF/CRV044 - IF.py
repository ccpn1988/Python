# 044 - GERENCIADOR DE PAGAMENTO

# DETERMINE O VALOR A SER PAGO PREÇO NORMAL
# A VISTA DINHEIRO/CHEQUE = 10% DESC
# A VISTA CARTAO = 5% DESC
# ATE 2X CARTAO = PREÇO NORMAL
# 3X OU MAIS = 20% JUROS
print('{:=^40}'. format(' LOJAS NEVES '))
valor = float(input('Informe o valor a ser pago: '))
print('''FORMAS DE PAGAMENTO: 
[ 1 ] - A VISTA DINHEIRO OU CHEQUE C/ 10% DESCONTO:
[ 2 ] - A VISTA NO CARTÃO C/ 5% DESCONTO:
[ 3 ] - CARTÃO 2X SEM JUROS:
[ 4 ] - CARTÃO 3X OU MAIS C/ 20% DE JUROS: ''')

# ESCOLHENDO A FORMA DE PAGAMENTO
pagamento = int(input('Informe a forma de pagamento: '))

# DEFININDO CALCULOS
if pagamento == 1:
    preço = valor - (valor * 10 / 100)
    print(f'Pagamento definido com DINHEIRO ou CHEQUE')
    print(f'O valor a pagar é de R${preço:.2f} já incluso 10% de desconto.')
elif pagamento == 2:
    preço = valor - (valor * 5 / 100)
    print(f'Pagamento definido via CARTÃO À VISTA')
    print(f'O valor a ser pago é de R${preço:.2f} já incluso 5% de desconto.')
elif pagamento == 3:
    preço = valor
    parcela = int(input('Digite a quantidade de parcelas: '))
    # VALIDANDO A QUANTIDADE DE PARCELAS, DE ACORDO COM A FORMA DE PAGAMENTO
    if parcela > 2:
        print(f'A qtd de parcelas informada, é maior do que a permita pela opção de pagamentos.')
    else:
         parcela = preço / 2
         print(f'Pagamento definido via CARTÃO EM 2X')
         print(f'O valor a ser pago é de R${preço:.2f} parcelado em {parcela}X de R${parcela:.2f}')
elif pagamento == 4:
    preço = valor + (valor * 20 / 100)
    parcelamento = int(input('Digite a quantidade de parcelas: '))
    # VALIDANDO A QUANTIDADE DE PARCELAS, DE ACORDO COM A FORMA DE PAGAMENTO
    if parcelamento < 3:
       print(f'A qtd de parcelas informada, é menor do que a permita pela opção de pagamentos.')
    else:
        parcela = preço / parcelamento
        print(f'Pagamento definido via CARTÃO PARCELADO COM JUROS DE 20%.')
        print(f'O valor a ser pago é de R${preço:.2f} parcelado em {parcelamento}X de R${parcela:.2f}')
else:
    print('Opção não identificada para Pagamentos')


