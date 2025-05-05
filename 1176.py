'''
Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.

Entrada
A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste. Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo termo da série de Fibonacci.

Saída
Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da série de Fibonacci.
'''
def fibo(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1 
    else:
        a = []
        a.append(0)
        a.append(1)
        for i in range(2, k+1):
            a.append(a[i - 1] + a[i-2])
        return a[len(a)-1]

n = int(input())

for i in range(n):
    k = int(input())
    
    print('Fib(' + str(k) + ') = ' + str(fibo(k)))
