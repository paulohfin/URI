n = 1
while n != 2:
    n1 = float(input())
    while n1 < 0 or n1 > 10:
        print('nota invalida')
        n1 = float(input())
    
    n2 = float(input())
    while n2 < 0 or n2 > 10:
        print('nota invalida')
        n2 = float(input())
    print('media = %.2f' %((n1 + n2)/2))
    print('novo calculo (1-sim 2-nao)')
    n = int(input())
    while n != 1 and n != 2:
        print('novo calculo (1-sim 2-nao)')
        n = int(input())