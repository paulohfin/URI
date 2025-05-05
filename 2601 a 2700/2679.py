'''
Para se preparar para os outros problemas, vamos fazer um teste. Dado um número X, retorne o menor número par maior do que X.

Entrada
Uma linha contendo um número  0 < X < 107.

Saída
Uma linha contendo a resposta do problema.
'''
while True:
    try:
        n = int(input())
        if (n + 1) %2 == 0:
            print(n+1)
        else:
            print(n+2)
    except EOFError:
        break 
