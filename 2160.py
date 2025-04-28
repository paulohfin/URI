while True:
    try:
        k = input()
        if len(k) <= 80:
            print('YES')
        else:
            print('NO')
    except EOFError:
        break