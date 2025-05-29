'''
A raposa Fink, muito esperta, precisa dividir meio a meio algumas comidas entre ele e Pica-Pau, mas ele está com muita fome e pensou em algo muito sagaz para sair ganhando nessa, a divisão vai ser da seguinte forma:

Primeiro ele coloca tudo sobre a mesa e começa a dividir: Um pra você. Um pra mim. Dois pra você. Um, dois pra mim. Três pra você. Um, dois, três pra mim... Dessa forma, se a quantidade inicial de comida fosse 12, ele terminaria com 10 e Pica-Pau com 2. Obs: Caso Fink não consiga terminar a última divisão, ele pode roubar do Pica-Pau.



Entrada
A entrada consistirá de uma série de linhas, cada uma contendo o número de comidas N (1 ≤ N ≤ 100000). O fim da entrada é indicado pelo número zero (0).

Saída
Para cada linha de entrada, você deverá imprimir quanta comida ficou com Fink e Pica-Pau ao final da divisão, separadas por um espaço.
'''
n = int(input())
while n > 0:
    p = 0
    f = 0
    c = 1
    while n > 0:
        p += 1
        n -= 1 
        for i in range(c):
            f += 1
            n -= 1
            if n < 0:
                n+=1 
                p-=1
        c+=1
    
    print(f,p)
    n = int(input())
