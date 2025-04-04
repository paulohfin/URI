while True:
    try:
        s, t, f = map(int, input().split(' '))
        
        print((s + t + f)%24)
    except EOFError:
        break