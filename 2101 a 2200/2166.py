'''
Uma das formas de calcular a raiz quadrada de um número natural é pelo método das frações periódicas continuadas. Esse método usa como denominador uma repetição de frações. Essa repetição pode ser feita uma quantidade específica de vezes.

Por exemplo, ao repetir 2 vezes a fração continuada para calcular a raiz quadrada de 2, temos a fórmula abaixo.



Sua tarefa é, dado o número N de repetições, calcular o valor aproximado da raiz quadrada de 2.

Entrada
A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de repetições do denominador na fração continuada.

Saída
A saída é o valor aproximado da raiz quadrada com 10 casas decimais.
'''
def raiz(n):
    if n > 0:
        return 1/(2+raiz(n-1))
    else: return 0
while True:
    try:
        n = int(input())
        
        print('%.10f' %(1 + raiz(n)))
    except EOFError:
        break
