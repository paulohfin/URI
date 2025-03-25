while True:
    try:
        d1, d2, d3 = map(int, input().split(' '))
        if d2 < d1:
            if d3 >= d2:
                print(':)')
            else:
                if d3 - d2 > d2 - d1:
                    print(':)')
                else:
                    print(':(')
        if d2 > d1:
            if d3 <= d2:
                print(':(')
            else:
                if d3 - d2 < d2 - d1:
                    print(':(')
                else:
                    print(':)')
        if d1 == d2:
            if d3 > d2:
                print(':)')
            else:
                print(':(')
    except EOFError:
        break 