# 056 - Ler o NOME, IDADE E SEXO DE 04 PESSOAS      #
# MEDIA DE IDADE                                    #
# NOME DO HOMEM MAIS VELHO                          #
# QTS MULHEREM TEM MENOS DE 20 ANOS                 #
#####################################################

# CONTADOR PARA MEDIA
somaidade = 0
# CONTADOR MAIOR IDADE HOMEM
maioridadehomem = 0
# VARIAVEL NOME HOMEM MAIS VELHO
nomehmaisvelho = ''
# CONTADOR QTD MULHERES COM IDADE ABAIXO DE 20
mulher20 = 0

for p in range(1, 5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input(f'Informe o nome: '))
    idade = int(input(f'Informe a idade : '))
    sexo = str(input(f'Informe o sexo da M/F: ')).strip()
    somaidade += idade

    # VERIFICANDO 1° PESSOA MASCULINA
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehmaisvelho = nome

        # VERIFICANDO NOVAMENTE SEXO MASCULINO E COMPARANDO A IDADE JA EM ARMAZENAMENTO DO HOMEM.
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehmaisvelho = nome

        # VERIFICANDO SE O SEXO E FEMININO E SE IDADE MENOR DO QUE 20 ANOS.
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

# CALCULANDO A MEDIA DE IDADE PELA QUANTIDADE DE PESSOAS ANALISADAS.
mediaidade = somaidade / 4

# IMPRIMINDO RESULTADOS.
print(f'A media de idade dos pesquisados é de {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem}anos e se chama {nomehmaisvelho}')
print(f'a quantidade de mulheres com idade menor a 20 anos é de {mulher20}')
