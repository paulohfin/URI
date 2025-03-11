def menor(a, b):
    if a < b:
        return a 
    else:
        return b

n = int(input())
while n != 0:
    for i in range(n):
        for j in range(n):
            string = '           ' + str(menor(menor(j + 1, i + 1),menor(n - i, n - j)))
            if j == n - 1:
                print(string[len(string) - 3:])
            else:
                print(string[len(string) - 3:], end=' ')
    n = int(input())
    #if n != 0:
    print()