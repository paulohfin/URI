'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
'''
n = int(input())
for i in range(n):
    a, b = map(int, input().split(' '))
    soma = 0
    if a > b:
        for j in range(b+1, a):
            if j % 2 != 0:
                soma += j
    else:
        for j in range(a+1, b):
            if j % 2 != 0:
                soma += j
    print(soma)
