while True:
    try:
        a = input()
        if a[0] == '-':
            n = float(a)
            print(f'{n:.4E}')
        else:
            print('+',end='')
            n = float(a)
            print(f'{n:.4E}')
        
    except EOFError:
        break 