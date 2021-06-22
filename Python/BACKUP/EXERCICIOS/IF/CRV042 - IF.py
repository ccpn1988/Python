# 042: LER 3 SEGMENTO DE RETAS E VALIDAR SE PODE CALCULAR UM TRIANGULO.
# TRIANGULO = CADA LADO TEM DE SER MENOR DO QUE A SOMA DOS OUTROS 2 LADOS
# EQUILATERO = TODOS LADOS IGUAIS
# ISOCELES = DOIS LADOS IGUAIS
# ESCALENO = TODOS OS LADOS DIFERENTES

print('-=-'* 10)
print('Analisador de Triângulos')
print('-=-'* 10)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os segmentos acima PODEM formar um triangulo, EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('Os segmentos acima PODEM formar um triangulo, ESCALENO')
    else:
        print('Os segmentos acima PODEM formar um triangulo, ISOSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo')
