while True:
    try:
        p1, p2 = map(float, input().split(' '))
        
        print('%.2f' %((p2 * 100 / p1) - 100),end='')
        print('%')
    except EOFError:
        break