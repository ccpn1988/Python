disciplina = input('Digitte o nome da disciplina: ')
nota_final = input('Digite a nota final entra 0 e 100: ')
semestre = input('Digite o semestre (1 a 4): ')
if disciplina == 'Geografia' and nota_final >= '70':
    print('Você foi aprovado....')
else:
    print('Lamento, voce precisa estudar mais...')

if disciplina == 'Geografia' or disciplina == 'Matematica' and nota_final >= '50' and int(semestre) != 1:
    print('Você foi aprovado em %s com média final %r' %(disciplina, nota_final))
else:
    print('Lamento, você precisa estudar mais....')
