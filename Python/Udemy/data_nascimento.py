## Programa Mês Nascimento

meses = ('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', ' SETEMBRO' , 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')
data_nasc = input('Insira dua data de nascimento no formato DD-MM-AAAA: ')

## Pegou como indice MM, porém na tupla (meses) o indice 5 seria o mês de JUNHO por isto -1
indice = int(data_nasc[3:5]) -1
mes = meses[indice]
print('Voce nasceu no mês de : ' , mes)
input('Pressione ENTER para sair do programa')

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    


