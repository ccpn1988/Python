# 043 - MASSA CORPORAL
# LER PESO ALTURA E CALCULE O IMC
# ABAIXO DE 18.5: ABAIXO DO PESO
# ENTRE 18.5 e 25 = PESO IDEAL
# 25 ATE 30 = SOBREPESO
# 30 ATE 40 = OBESIDADE
# ACIMA DE 40 OBESIDADE MORBIDA

alt = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / (alt * alt)

if imc < 18.5:
    print(f'Você esta ABAIXO DO PESO!!! Seu IMC é de {imc:.2f}')
elif imc >= 18.5 and imc <= 25:
    print(f'Você está com PESO IDEAL!!! Seu IMC é de {imc:.2f}')
elif imc >= 25 and imc <= 30:
    print(f'VocÊ está com SOBREPESO!!!! Seu IMC é de {imc:.2f}')
elif imc >= 30 and imc <=40:
    print(f'VocÊ esta com OBESIDADE!!! Seu IMC é de {imc:.2f}')
else:
    print(f'Você esta com OBESIDADE MORBIDA!!! Seu IMC é de {imc:.2f}')

