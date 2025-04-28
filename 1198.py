while True:
    try:
        a, b = map(int, input().split(' '))
        dif = b - a
        if dif > 0:
            print(dif)
        else:
            print(-dif)
    except EOFError:
        break