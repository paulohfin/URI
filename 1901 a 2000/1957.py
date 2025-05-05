'''
Os dados armazenados no computador estão em binário. Uma forma econômica de ver estes números é usar a base 16 (hexadecimal).

Sua tarefa consiste em escrever um programa que, dado um número natural na base 10, mostre sua representação em hexadecimal.

Entrada
A entrada é um número inteiro positivo V na base 10 (1 ≤ V ≤ 2 x 109).

Saída
A saída é o mesmo número V na base 16 em uma única linha (não esqueça do caractere de fim-de-linha). Use letras maiúsculas, conforme os exemplos.
'''
def printa(n):
    if n < 10:
        print(n, end='')
    elif n == 10:
        print('A', end='')
    elif n == 11:
        print('B', end='')
    elif n == 12:
        print('C', end='')
    elif n == 13:
        print('D', end='')
    elif n == 14:
        print('E', end='')
    elif n == 15:
        print('F', end='')

def hexa(n):
    if n > 15:
        r = n% 16
        hexa(int(n/16))
        printa(r)
    else:
        printa(n)

while True:
    try:
        n = int(input())
        
        hexa(n)
        print()
    except EOFError:
        break 
