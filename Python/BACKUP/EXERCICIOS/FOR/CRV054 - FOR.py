# 054 - LER ANO DE NASCIMENTO DE 07 PESSOAS E MOSTRAR QUANTAS PESSOAS SÂO MAIORES DE IDADE.

from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano {pessoa}° a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print(f'Ao todo tivemos {tmaior} pessoas maiores de idade')
print(f'E também tivemos {tmenor} pessoas menores de ideade')
