# 036 - APROVANDO EMPRESTIMOS
# APROVE UM EMPRESTIMO BANCARIO PARA COMPRAR UMA CASA.
# PERGUNTE O VALOR DA CASA, O SALARIO DO COMPRADOR E OS ANOS DE FINANCIAMENTO
# CALCULE O VALOR DA PRESTAÇÃO, NAO EXECENDENDO 30% DO SALARIO, SE NAO O EMPRESTIMO SERA NEGADO.

from time import sleep
print('-=' *18)
print('\033[31mCalculando Financiamento Imobiliario\033[m')
print('-=' *18)

salario = float(input('Informe o salario a ser calculado eo financiamento: R$ '))
imovel = float(input('Informe o valor do imóvel a ser financiado: R$ '))
anos = int(input('Informe q quantidade de anos para pagamento: '))
limitepar = salario * 30 / 100
parcela = imovel / (anos * 12)

print('CALCULANDO FINANCIAMENTO')
sleep(1)

if parcela > limitepar:
    print(f'\033[33m FINANCIAMENTO APROVADO.....\033[m')
    print(f'O imóvel no valor de R$ {imovel:.2f} será financiado em {anos} anos com parcelas de R$ {parcela:.2f}')
else:
    print(f'\033[31m FINANCIAMENTO NEGADO....\033[m', end=' ')
    print(f'O valor das parcelas de R$ {parcela:.2f}, ultrapassam 30% do seu salário R$ {parcela:.2f}')