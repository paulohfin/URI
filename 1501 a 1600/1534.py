'''
Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido.

Entrada
A entrada contém vários casos de teste e termina com EOF. Cada caso de teste é composto por um único inteiro N (3 ≤ N < 70), que determina o tamanho (linhas e colunas) de uma matriz que deve ser impressa.

Saída
Para cada N lido, apresente a saída conforme o exemplo fornecido.
'''
while True:
    try:
        n = int(input())
        
        for i in range(n):
            for j in range(n):
                if i + j == n-1:
                    print(2, end='')
                elif i == j:
                    print(1, end='')
                else:
                    print(3, end='')
            print()
    except EOFError:
        break
