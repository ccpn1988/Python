qtd_km = float(input('Qual a KM percorrida na viagem '))
qtd_dias = int(input('Qual a quantidade de dias da locacao do veiculo '))

diaria = 60
vlr_km = 0.15

km_dia = qtd_km / qtd_dias
custo_dia = round((km_dia * vlr_km)+diaria,2)
custo_km = qtd_km * vlr_km

total = (diaria * qtd_dias) + custo_km

print('O custo por dia da viagem foi de: ', custo_dia)
print('O custo por KM da viagem foi de: ', custo_km)
print('O custo total da viagem foi de: ', total)

input('Pressione Enter para sair do Programa')