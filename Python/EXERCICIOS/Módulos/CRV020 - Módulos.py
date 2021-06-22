# SORTEANDO UMA ORDEM NA LISTA
# https://docs.python.org/3.8/library/random.html#random.shuffle
import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)

print('A ordem de apresentação sera: ')
print(alunos)