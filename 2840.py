while True:
    try:
        r, l = map(int, input().split(' '))
        v = 4/3 * 3.1415 * r * r * r
        print(int(l / v))
    except EOFError:
        break