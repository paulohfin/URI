def maior(a, b):
    if a > b:
        return a 
    else:
        return b

n = int(input())
while n != 0:
    for i in range(n):
        for j in range(n):
            string = '           ' + str(maior(i - j, j - i) + 1)
            if j == n - 1:
                print(string[len(string) - 3:])
            else:
                print(string[len(string) - 3:], end=' ')
    n = int(input())

    print()