'''
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.


'''
def menor(a, b):
    if a < b:
        return a 
    else:
        return b

n = int(input())
while n != 0:
    for i in range(n):
        for j in range(n):
            string = '           ' + str(menor(menor(j + 1, i + 1),menor(n - i, n - j)))
            if j == n - 1:
                print(string[len(string) - 3:])
            else:
                print(string[len(string) - 3:], end=' ')
    n = int(input())
    #if n != 0:
    print()
