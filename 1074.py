n = int(input())

for i in range(n):
    a = int(input())
    if a == 0:
        print('NULL')
    else:
        if a % 2 == 0:
            print('EVEN',end=' ')
        else:
            print('ODD',end=' ')
        if a > 0:
            print('POSITIVE')
        else:
            print('NEGATIVE')