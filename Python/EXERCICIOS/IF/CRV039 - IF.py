# 039 - ALISTAMENTO MILITAR
# SE AINDA VAI SE ALISTAR
# SE É PARA SE ALISTAR
# SE JÁ PASSOU O TEMPO
# MOSTRAR O TEMPO QUE FALTA OU PRAZO EXCEDENTE

from datetime import date
from time import sleep
print('-=-' * 11)
print('\033[32m VALIDANDO PRAZO PARA ALISTAMENTO\033[m ')
print('-=-' * 11)

nasc = int(input('Informe o ano de nascimento: '))
# ANO ATUAL
ano = date.today().year
idade = int(ano - nasc)
print()
print('\033[32mVERIFICANDO ALISTAMENTO...\033[m ')
print()
sleep(1)

print(f'Quem nasceu em {nasc} tem {idade} anos em {ano}')

if idade == 18:
    print(f'Você tem {idade} anos compareça para efetuar o seu \033[32mALISTAMENTO MILITAR\033[m ')
elif idade > 18:
    print(f'Seu período de alistamento ja passou à {(idade) - 18} anos')
    print(f'Seu ano de alistamento foi em: {nasc + 18}')
elif idade < 18:
    print(f'Seu período de alistamento ainda não chegou, faltam {18 - (idade)} ano(s)')
    print(f'Seu ano de alistamento será em: {nasc + 18}')


