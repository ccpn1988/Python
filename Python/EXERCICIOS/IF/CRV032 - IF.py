# ANO BISSEXTO
from datetime import date
ano = int(input('Digite o ano ao qual quer analisar? Coloque 0 para atualizar o ano atual. '))
if ano == 0:
    # ANO ATUAL
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO')
else:
    print(f'O ano de {ano} não é BISSEXTO')