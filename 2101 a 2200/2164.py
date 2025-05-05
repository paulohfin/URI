'''
A fórmula de Binet é uma forma de calcular números de Fibonacci.



Sua tarefa é, dado um natural n, calcular o valor de Fibonacci(n) usando a fórmula acima.

Entrada
A entrada é um número natural n (0 < n ≤ 50).

Saída
A saída é o valor de Fibonacci(n) com 1 casa decimal utilizando a fórmula de Binet dada.
'''
import math

def fibo(n):
    return (math.pow((1 + math.sqrt(5))/2,n) - math.pow((1 - math.sqrt(5))/2,n))/math.sqrt(5)

while True:
    try:
        n = int(input())
        
        print('%.1f'%(fibo(n)))
    except EOFError:
        break
