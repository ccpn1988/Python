# LER A VELOCIDADE DE UM CARRO, SE MAIOR QUE 80KM/H, INFORME QUE FOI MULTADO E O VALOR É DE 7.00 A CADA KM ACIMA.

velocidade = float(input('Digite a velocidade a ser verificada: '))
limite = int(70)

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print(f'Você excedeu o limite de {limite:.2f}KM/h, sua multa será no valor de: R$ {multa:.2f}')
else:
    print(f'Sua velocidade {velocidade}KM/h, esta dentro do limite de: {limite}KM/h ')