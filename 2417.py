
while True:
    try:
        cv, ce, cs, fv, fe, fs = map(int, input().split(' '))
        
        Cs = 3 * cv + ce 
        Fs = 3 * fv + fe 
        
        if Cs > Fs:
            print('C')
        elif Cs < fs:
            print('F')
        elif cs > fs:
            print('C')
        elif fs > cs:
            print('F')
        else:
            print('=')
    except EOFError:
        break