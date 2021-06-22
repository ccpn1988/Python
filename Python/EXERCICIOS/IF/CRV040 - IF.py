# MEDIAS Dos ALUNOS
# LER 2 NOTAS E CALCULA A MEDIA
# 5.0 REPROVADO
# 5.0 e 6.9 RECUPERAÇÃO
# 7.0 APROVADO

from time import sleep

# CABEÇALHO DO EXERCICIO
print('-=-' * 11)
print('\033[31m EXERCICIO 40 - CALCULO DE MÉDIAS\033[m')
print('-=-' * 11)

# SOLICITANDO AS NOTAS A SEREM APURADAS
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# FORMULA PARA CALCULAR MEDIA
media = (n1 + n2) /2

print('Calculando as médias...')
sleep(1)

# EXECUTANDO AS CONDIÇÔES CONFORME AS MEDIAS

if media < 5.0:
    print(f'\033[31m REPROVAOO!!!\033[m, sua média foi {media}')
elif media >= 5.0 and media <= 6.9:
    print(f'\033[34m RECUPERAÇÃO!!!\033[m, sua média foi {media}')
elif media >= 7.0:
    print(f'\033[32m APROVADO!!!!\033, sua média foi {media}')


