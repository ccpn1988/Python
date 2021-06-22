# 071 -  CAIXA ELETRONICO
# PERGUNTE O VALOR A SER SACADO
# INFORMAR QUANTAS CEDULAS DE CADA VALOR SERAO ENTREGUES
# CAIXA POSSUI CEDULAS DE: 50,20,10,1
print('=' * 30)
print('{:^30}'.format("BANCO YOUTUBE"))
print('=' * 30)

valor = int(input('Informe o valor para saque: R$ '))
total = valor
# CONSIDERANDO A MAIOR CEDULA
cedula = 50
totalced = 0
while True:
# VERIFICA QTS VEZES CONSEGUE RETIRAR O VALOR DA CEDULA DO TOTAL
# DEBITO O VALOR DE ACORDO COM A CEDULA
# CONTAGEM DA QTD DE CEDULA USADA NO SAQUE
    if total >= cedula:
        total -= cedula
        totalced += 1
# NÃO IMPRIMIR CEDULAS SEM USO
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R$ {cedula:.2f}')
# FAZ TRATATIVAS COM AS CEDULAS, SE FOR IGUAL AO VALOR DA CEDULA, MUDA PARA PROXIMA CEDULA
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0 # QUANDO MUDAR A CEDULA DEVE SER ZERADO O CONTADOR
        if total == 0:
            break