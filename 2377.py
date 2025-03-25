while True:
    try:
        L, D = map(int, input().split(' '))
        K, P = map(int, input().split(' '))
        
        print(K * L + int(L / D) * P)
    except EOFError:
        break