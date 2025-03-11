while True:
    n = int(input())

    if n == 0: break


    for i in range(n):
        a, b, c, d, e = map(int, input().split(' '))
        res = ''
        if a <= 127:
            res += 'A'
        if b <= 127:
            res += 'B'
        if c <= 127:
            res += 'C'
        if d <= 127:
            res += 'D'
        if e <= 127:
            res += 'E'
        if len(res) == 1:
            print(res)
        else:
            print('*')