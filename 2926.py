while True:
    try:
        n = int(input())
        print('Ent',end='')
        for i in range(n):
            print('a',end='')
        print('o eh N',end='')
        for i in range(n):
            print('a',end='')
        print('t',end='')
        for i in range(n):
            print('a',end='')
        print('l!')
    except EOFError:
        break 