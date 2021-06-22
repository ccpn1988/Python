meses = ('JAN', 'FEV', 'MAR', 'ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ')
nasc = input('Informe sua data de nascimento com o formato DD-MM-AA : ')

indice = int(nasc[3:5])-1

mes = meses[indice]
print('Seu mês de nascimento é : ', mes)
           
