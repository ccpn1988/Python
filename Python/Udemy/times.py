
times = ('Corinthians', 'Palmeiras', 'São Paulo', 'Santos')
titulos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
seu_time = input('Digite a quantidade de títulos Paulistas do seu time : ')
campeao = int(seu_time[0:2]) 

for i in titulos:
    i = campeao
    
if i >=24:
    print('Você torce para o : ', times[0])
elif i >=23:
    print('Você torce para o : ',times[1])
elif i == 22:
    print('Você torce para o : ', times[3])
else:
    print('Você torce para o : ' , times[2])

input("Pressione o botão Enter para sair")    
    
