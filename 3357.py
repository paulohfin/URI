while True:
    try:
        N, L, Q = map(float, input().split(' '))
        p = input().split(' ')
        i = 0
        while L >= Q:
            L -= Q
            i += 1
            i %= len(p)
        print(p[i], '%.1f' %L)
            
    except EOFError:
        break