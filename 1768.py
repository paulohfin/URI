while True:
    try:
        n = int(input())
        i = 1 
        while i <= n:
            for j in range(int((n+1)/2 - (i + 1)/2)):
                print(' ', end='')
            for j in range(i):
                print('*', end='')
            print()
            i += 2
        i = 1 
        while i <= 4:
            for j in range(int((n+1)/2 - (i + 1)/2)):
                print(' ', end='')
            for j in range(i):
                print('*', end='')
            print()
            i += 2
        print() 
    except EOFError:
        break