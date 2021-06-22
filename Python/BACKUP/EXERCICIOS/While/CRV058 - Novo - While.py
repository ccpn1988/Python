from random import randint
computador = randint(0,10)
print('Sou seu computador.... Acabei de escolher um numero entre 0 e 10... ')
print('Sera que vocÊ consegue adivinhar? ')
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos.... Tente mais uma vez.')
print(f'Acertou após {palpite} palpites')

