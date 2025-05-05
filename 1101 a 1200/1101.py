'''
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.
'''
a, b = map(int, input().split(' '))

while a > 0 and b > 0:
    if b < a:
        max = a
        a = b
        b = max
    soma = 0
    for i in range(a, b+1):
        soma += i
        print(i, end=' ')
    print('Sum=' + str(soma))
    a, b = map(int, input().split(' '))
