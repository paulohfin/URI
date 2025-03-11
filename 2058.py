while True:
    try:
        n = int(input())

        print(n - 2)
    except EOFError:
        break