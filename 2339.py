while True:
    try:
        c, p, f = map(int, input().split(' '))
        
        if c * f <= p:
            print('S')
            
        else:
            print('N')
    except EOFError:
        break