# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

f = float(input('Informe a temperatura em °F: '))
c = 5 * ((f - 32) / 9)
print(c)