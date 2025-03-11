while True:
    try:
        a, b = map(int, input().split(' '))
        if a == b:
            break
        if a > b:
            print('Decrescente')
        if b > a:
            print('Crescente')
            
    except EOFError:
        break