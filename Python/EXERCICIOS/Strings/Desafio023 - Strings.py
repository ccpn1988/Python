# DIGITE UM NUMERO E O SEPARE POR UNIDADE, DEZENA, CENTENA, MILHAR

num = int(input('Digite um numero com até 4 digitos... '))
n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# FORMATO STRING - DA ERRO SE NAO TIVER 4 DIGITOS
# print(f'Analisando o número {num} em string')
# print(f'Unidade: {n[3]}')
# print(f'Dezena: {n[2]}')
# print(f'Centena: {n[1]}')
# print(f'Milhar: {n[0]}')

print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')