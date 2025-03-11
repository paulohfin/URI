n = int(input())

for i in range(n):
    x, y = map(int, input().split(' '))
    soma = 0
    x1 = 0
    while x1 < y:
        if x % 2 != 0:
            soma += x
            x1 += 1
        x += 1
    print(soma)