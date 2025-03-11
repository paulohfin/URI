n = int(input())
a = 0
b = 1
for i in range(n):
    if i == 0:
        if i == n-1:
            print(a)
        else:
            print(a, end=' ')
    elif i == 1:
        if i == n-1:
            print(b)
        else:
            print(b, end=' ')
    else:
        temp = a + b
        a= b
        b = temp
        if i == n-1:
            print(temp)
        else:
            print(temp, end=' ')
        