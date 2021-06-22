# WHILE - EXECUTA O LOOP ENQUANTO FOR VERDADE A CONDIÇÂO
# USADO QUANDO NÃO TEM LIMTIE FINAL
# FOR USADO QD TEM INICIO,FIM.

# WHILE NOT MAÇA:
    #passo
#pega

# for c in range(1, 10):
#     print(c)
# print('FIM')

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

n = 1
# ENQUANTO A CONDIÇÂO DIGITADA NAO FOR 0 O LOOP CONTINUA
while n != 0:
    n = int(input('Digite um número: '))
print('ENCERRANDO')

r = 'S'
# ENQUANTO r FOR IGUAL S EXECUTA
while r == 'S':
    n = int(input('Digite um número:'))
    r = str(input('Quer continua [S/N] ')).upper()
print('FIM')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} numeros impares.')