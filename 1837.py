while True:
    try:
        a, b = map(int, input().split(' '))
        r = a%b
        if r < 0:
            r -= b
        q = int((a - r) / b)
        print(q,r)
        
    except EOFError:
        break