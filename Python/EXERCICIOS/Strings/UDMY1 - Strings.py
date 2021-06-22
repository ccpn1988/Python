from time import sleep
nome = str(input('Digite seu nome... '))
sobre_pai = str(input('Digite seu sobrenome Paterno... '))
sobre_mae = str(input('Diigte seu sobrenome Materno.. '))

print('Analisando e concatenando seu nome.. ')
sleep(1)
nome_full = nome + ' ' + sobre_pai + ' ' + sobre_mae
print(nome_full)

print('Pegando as iniciais do nome e sobrenome informado... ')
print(nome[0] + sobre_pai[0] + sobre_mae[0])