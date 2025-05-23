'''
Há muitos jogos divertidos que usam pequenas varetas coloridas. A variante usada neste problema envolve a construção de retângulos. O jogo consiste em, dado um conjunto de varetas de comprimentos variados, desenhar retângulos no chão, utilizando as varetas como lados dos retângulos, sendo que cada vareta pode ser utilizada em apenas um retângulo, e cada lado de um retângulo é formado por uma única vareta. Nesse jogo, duas crianças recebem dois conjuntos iguais de varetas. Ganha o jogo a criança que desenhar o maior número de retângulos com o conjunto de varetas.

Dado um conjunto de varetas de comprimentos inteiros, você deve escrever um programa para determinar o maior número de retângulos que é possível desenhar.

Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro N que indica o número de diferentes comprimentos de varetas (1 ≤ N ≤ 1.000) no conjunto. Cada uma das N linhas seguintes contém dois números inteiros Ci e Vi , representando respectivamente um comprimento (1 ≤ Ci ≤ 10.000) e o número de varetas com esse comprimento (1 ≤ Vi ≤ 1.000). Cada comprimento de vareta aparece no máximo uma vez em um conjunto de teste (ou seja, os valores Ci são distintos). O ﬁnal da entrada é indicado por N = 0.

Saída
Para cada caso de teste da entrada seu programa deve produzir uma única linha na saída, contendo um número inteiro, indicando o número máximo de retângulos que podem ser formados com o conjunto de varetas dado.
'''
n = int(input())

while n != 0:
    c = []
    v = []
    for i in range(n):
        ci, vi = map(int, input().split(' '))
        c.append(ci)
        v.append(vi)
    if n == 1:
        print(int(v[0] / 4))
    else:
        soma = 0
        for i in range(n):
            soma += int(v[i] / 2)
        print(int(soma/2))
    n = int(input())
