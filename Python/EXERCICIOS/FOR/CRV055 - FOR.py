# LER O PESO DE 5 PESSOAS E MOSTRE O MAIOR E O MENOR
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Digite o {pessoa}° peso: '))
    # SEMPRE NO 1° LAÇO O VALOR SERA O MAIOR E O MENOR POIS NAO HA REFERENCIA
    if pessoa == 1:
        maior = peso
        menor = peso
    # A PARTIR DO 2° LAÇO COMEÇA EFETUAR A VALIDAÇÃO
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}KG')
print(f'O menor peso lido foi de {menor}KG')
