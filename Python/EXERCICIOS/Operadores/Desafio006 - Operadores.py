# DIGITE UM NUMERO E MOSTRE SEU DOBRO TRIPLO E RAIZ QUADRADA

# METODO DE RAIZ QUADRADA
import math

num1 = int(input('Digite um numero... '))
dobro = num1 * 2
triplo = num1 * 3
rquad = math.sqrt(num1)

print(f'O numero digitado foi {num1}')
print(f'O dobro de {num1} é {dobro}')
print(f'O triplo de {num1} é {triplo}')
print(f'A raiz quadrada de {num1} é {rquad:.2f}')