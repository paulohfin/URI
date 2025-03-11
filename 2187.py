cont = 1

n = int(input())
while n != 0:
    print('Teste', cont)
    n50 = int(n / 50)
    n %= 50
    n10 = int(n / 10)
    n %= 10
    n5 = int(n / 5)
    n %= 5
    n1 = n
    print(n50, n10, n5, n1)
    print()
    cont += 1
    n = int(input())