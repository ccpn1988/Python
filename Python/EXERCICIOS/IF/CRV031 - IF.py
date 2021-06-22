# PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM E CALCULE A PASSAGEM
# 0.50 por KM até 200KM
# 0.45 por KM MAIS LONGOS

distancia = float(input('Informe a distância de sua viagem: '))

if distancia <= 200:
    v1 = distancia * 0.50
    print(f'Você percorreu {distancia:.2f}KM e o valor da sua passagem é de: R$ {v1:.2f}')
else:
    v1 = distancia * 0.45
    print(f'VocÊ percorreu {distancia:.2f}KM e o valor de sua passagem é de: R$ {v1:.2f}')

##############################################################################################################################

# v1 = distancia * 0.50 if distancia <= 200 else v1 = distancia * 0.45