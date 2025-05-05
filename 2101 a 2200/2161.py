'''
Uma das formas de calcular a raiz quadrada de um número natural é pelo método das frações periódicas continuadas. Esse método usa como denominador uma repetição de frações. Essa repetição pode ser feita uma quantidade específica de vezes.

Por exemplo, ao repetir 2 vezes a fração continuada para calcular a raiz quadrada de 10, temos a fórmula abaixo.



Sua tarefa é, dado o número N de repetições, calcular o valor aproximado da raiz quadrada de 10.

Entrada
A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de repetições do denominador na fração continuada.

Saída
A saída é o valor aproximado da raiz quadrada com 10 casas decimais.
'''
def frac(n):
    if n > 1:
        return 6+1/frac(n-1)
    else:
        return 6

while True:
    try:
        k = int(input())
        if k > 0:
            print('%.10f'%(3 + 1/frac(k)))
        else: print('%.10f'%3)
    except EOFError:
        break
