# 068 - JOGAR PAR OU IMPAR COM COMPUTADOR
# INTERROMPER O JOGO QUANDO O JOGADOR PERDER
# MOSTRAR A QTD DE VITORIAS DO COMPUTADOR

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    # COMPUTADOR ESCOLHENDO
    comp = randint(0,10)
    # SOMANDO OS VALORES DIGITADOS PARA VALIDAR
    total = jogador + comp
    # INCIANDO TIPO (P/I)
    tipo = ' '
    # VALIDANDO SE É PAR OU IMPAR
    while tipo not in 'PI':
        # DEFININDO MAIUSCULO,SEM ESPAÇOS 1 POSIÇAO CASO DIGITE PAR OU IMPAR
        tipo = str(input('Par ou impar? [P/I]: ')).strip().upper()[0]

    # IMPRIMINDO OS VALORES DIGITADOS E VERIFICANDO O TIPO (PAR ou IMPAR)
    print(f'Você jogou {jogador} e o computador jogou {comp}, Totalizando {total}')
    print('DEU PAR ' if total % 2 == 0 else 'DEU IMPAR')

    # VALIDANDO CONDIÇAO PAR
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            # INCREMENTANDO A QTD DE VITORIAS
            v += 1
        else:
            print('Voc PERDEU')
            break

    # VALIDANDO CONDIÇÂO IMPAR
    elif tipo == 'I':
        if total % 3 == 0:
            print('Você Venceu')
            # INCREMENTANDO A QTD DE VITORIAS
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente....')
print(f'Game Over.... Voce venceu {v}')



