# import modulo - IMPORTA TODO CONTEUDO
# from módulo import item - IMPORTA APENAS O CONTEUDO ESPECIFICO
# from módulo import item, item - IMPORTA APENAS O CONTEUDO ESPECIFICO

# BIBLIOTECAS

# MATH = MATEMATICA

import emoji

# import math from ceil = ARREDONDA P CIMA
# import math from floor - ARREDONDA P BAIXO
# import math from trunc - TRUNCA O VALOR DA VIRGULA P FRENTE
# import math from pow - POTENCIA
# import math from sqrt - RAIZ QUADRADA
# import math from factorial - FATOR
# https://docs.python.org/3.8/library/math.html
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} é igual {raiz}')
print(f'A raiz de {num} é igual {math.ceil(raiz)}')
print(f'A raiz de {num} é igual {math.floor(raiz)}')
print(f'A raiz de {num} é igual {math.trunc(raiz)}')

import random
num1 = random.random()
num1 = random.randint(1,50)
print(num1)
