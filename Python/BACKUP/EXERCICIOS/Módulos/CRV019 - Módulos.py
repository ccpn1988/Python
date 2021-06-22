# SORTEANDO UM ITEM DE UMA LISTA
# https://docs.python.org/3.8/library/random.html#random.choice

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

alunos = [n1, n2, n3, n4]
escolhido = random.choice(alunos)
print(f'O aluno escolhido foi {escolhido}')
