def hexa(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1 
        b = 2
        for i in range(n - 2):
            temp = a + b
            a = b
            b = temp
        return temp

while True:
    try:
        n = int(input())
        if n == 0:
            break
        print(hexa(n))
    except EOFError:
        break