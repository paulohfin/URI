while True:
    try:
        a, b, c = map(int, input().split(' '))
        
        if a == b or a == c or b == c or a + b == c or b + c == a or a + c == b:
            print('S')
        else:
            print('N')
    except EOFError:
        break 