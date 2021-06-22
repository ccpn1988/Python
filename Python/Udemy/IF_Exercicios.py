nome = input('Informe seu nome para processamento das notas : ')
nota1 = float(input('Informe a nota da 1° prova : '))
nota2 = float(input('Informe a nota da 2° prova : '))
faltas =  int(input('Informe a quantidade de faltas : '))
media = (nota1+nota2) /2
assid = (20-faltas)/20

if assid >= 0.7 and media >= 6.0:
    resultado = 'Aprovado'


elif media < 6 and assid < 0.7:
    resultado = 'Reprovador por notas e faltas'

elif media < 6:
    resultado = 'Reprovado por média'

elif assid < 0.7:
    resultado = 'Reprovador por faltas'

else:
    print('Erro ')

print('Nome : ', nome)
print('Media: ', media)
print('Assiduidade:', assid)
print('Resultado :', resultado)
    


input('Tecle ENTERT para sair')


      
            
