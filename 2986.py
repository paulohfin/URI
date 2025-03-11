def degrau(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        a = 1 
        b = 2
        c = 4
        for i in range(n - 3):
            temp = a + b + c
            a = b
            b = c
            c = temp
            c %= 1000000007
        return c

while True:
    try:
        n = int(input())
        print(degrau(n))
    except EOFError:
        break