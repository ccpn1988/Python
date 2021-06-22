# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

base = int(input('Digite a base (b) do quadrado a ser calculada: '))
alt = int(input('Digite a altura (h) do quadrado a ser calculada: '))
area = base * alt
dobro = area * 2

print(f'A área do quadrado com os dados informado é de : {area}m e seu dobro: {dobro}m')