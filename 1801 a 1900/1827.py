'''
Neste programa seu trabalho é ler um valor inteiro que será o tamanho da matriz quadrada (largura e altura) que será preenchida da seguinte forma: a parte externa é preenchida com 0, a parte interna é preenchida com 1, a diagonal principal é preenchida com 2, a diagonal secundária é preenchida com 3 e o ponto central contém o valor 4, conforme os exemplos abaixo.

Obs: o quadrado com '1' sempre começa na posição tamanho/3, tanto na largura quanto quanto na altura. A linha e a coluna começam em zero (0).

Entrada
A entrada contém vários casos de teste e termina com EOF (fim de arquivo. Cada caso de teste consiste de um valor inteiro ímpar N (5 ≤ N ≤ 101) que é o tamanho da matriz.

Saída
Para cada caso de teste, imprima a matriz correspondente conforme o exemplo abaixo. Após cada caso de teste, imprima uma linha em branco.
'''
while True:
    try:
        n = int(input())
        
        for i in range(n):
            for j in range(n):
                if i == int(n/2) and j == int(n/2):
                    print('4',end='')
                elif i+1 > n/3 and j+1 > n/3 and i < 2*n/3 and j < 2*n/3:
                    print('1',end='')
                elif i + j == n - 1:
                    print('3',end='')
                elif i == j:
                    print('2',end='')
                else:
                    print('0',end='')
            print()
        print()
    except EOFError:
        break 
