# 040 - CATEGORIAS
# DEFINIR CATEGORIAS DE ACORDO COM NASC
# ATE 9 ANOS = MIRIM
# ATE 14 ANOS = INFANTIL
# ATE 19 ANOS = SENIOR
# ACIMA 20 ANOS = MASTER

from datetime import date
from time import sleep
print('-=-' * 7)
print('\033[31m DEFININDO CATEGORIAS \033[m')
print('-=-' * 7)

# SOLICITANDO NASCIMENTO PARA CALCULO
nasc = int(input('Informe seu ano de nascimento: '))

# DEFININDO ANO ATUAL
ano = date.today().year

# DEFININDO CATEGORIA
idade = ano - nasc

if idade <= 9:
    print(f'Você tem {idade} anos e faz parte da categoria\033[31m MIRIM \033[m')
elif idade > 9 and idade <= 14:
    print(f'Voce tem {idade} anos e faz parte da categiria\033[32m INFANTIL \033[m')
elif idade > 14 and idade <= 19:
    print(f'Voce tem {idade} anos e faz parte da categiria\033[33m JUNIOR \033[m')
elif idade == 20:
    print(f'Voce tem {idade} anos e faz parte da categiria\033[34m SÊNIOR \033[m')
else:
    print(f'Voce tem {idade} anos e faz parte da categiria\033[35m MASTER \033[m')


