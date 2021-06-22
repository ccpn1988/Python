# 050 - ler 6 numeros inteiros, somar apenas os valores pares.
somar = 0
cont = 0
for i in range(0, 7):
    num = int(input(f'Digite o {i} numero: '))
    if num % 2 == 0:
        somar += num
        cont += 1
print(f'Você informou {cont} numeros pares e a soma foi: {somar} ')