while True:
    try:
        n = int(input())
        for i in range(n):
            if i < n - 1:
                print("Ho ", end='')
            else:
                print("Ho!")
    except EOFError:
        break