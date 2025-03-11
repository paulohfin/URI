while True:
    try:
        v, t = map(int, input().split(' '))

        print(int(v * t * 2))
    except EOFError:
        break