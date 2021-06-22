# CALCULE A MEDIA
# TOTAL DE 20 AULAS NAO PODENDO TER FREQUENCIA MENOR DO QUE 70% E MEDIA 6.0
# IMPRIMIT (NOME - MEDIA - % DE PRESENÇA - RESULTADO)

nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
faltas = int(input('Digite a quantidade de faltas: '))
presença = int(20 - faltas)/20
media = (n1 + n2) / 2

if presença >= 14:
    if media >= 6.0:
        print(f'O aluno {nome} foi aprovado com média {media} e {faltas} faltas')
    else:
        print(f'O aluno {nome} reprovado com media: {media}')

elif presença < 14:
    if media >= 6.0:
        print(f'O aluno {nome} foi reprovado por {faltas} faltas')
    else:
        print(f'O aluno {nome} foi reprovado pela media {media} e {faltas} faltas')
else:
    print('Dados incorretos para analise...')
