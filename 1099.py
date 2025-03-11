n = int(input())
for i in range(n):
    a, b = map(int, input().split(' '))
    soma = 0
    if a > b:
        for j in range(b+1, a):
            if j % 2 != 0:
                soma += j
    else:
        for j in range(a+1, b):
            if j % 2 != 0:
                soma += j
    print(soma)