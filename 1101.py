a, b = map(int, input().split(' '))

while a > 0 and b > 0:
    if b < a:
        max = a
        a = b
        b = max
    soma = 0
    for i in range(a, b+1):
        soma += i
        print(i, end=' ')
    print('Sum=' + str(soma))
    a, b = map(int, input().split(' '))