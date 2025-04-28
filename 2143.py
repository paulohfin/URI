n = int(input())

while n != 0:
    for i in range(n):
        k = int(input())
        if k % 2 == 0:
            print(k * 2 - 2)
        else:
            print(k * 2 - 1)
    n = int(input())