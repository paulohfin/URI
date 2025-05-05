'''
Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N.
'''
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)
        
valor = int(input())

print(fatorial(valor))
