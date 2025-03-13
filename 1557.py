import math
n = int(input())

while n != 0:
    tam = int(math.pow(4, n-1))
    space = ''
    for i in range(len(str(tam))):
        space += ' '
    a = 1
    for i in range(n):
        b = a
        for j in range(n):
            valor = space + str(b)
            #print('-',valor, len(valor), len(valor) - len(str(tam)), end=' ')
            if j == n-1:
                print(valor[len(valor) - len(str(tam)):], end='')
            else:
                print(valor[len(valor) - len(str(tam)):], end=' ')
            b *= 2
        a *= 2
        print()
    
    print()
    n = int(input())