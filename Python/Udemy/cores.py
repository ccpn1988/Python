# Exercícios Dicionarios
cores = {'vermelho' : 'red', 'verde': 'green', 'azul': 'blue', 'amarelo':'yellow'}
cor = input('Digite a cor desejada : ' ).lower() #reconhecerá apenas de forma minuscula
traducao = cores.get(cor,'Esta cor não existe')
print(traducao)
##print(cores.get(dados,' Esta cor não existe'))
