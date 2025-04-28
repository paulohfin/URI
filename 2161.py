def frac(n):
    if n > 1:
        return 6+1/frac(n-1)
    else:
        return 6

while True:
    try:
        k = int(input())
        if k > 0:
            print('%.10f'%(3 + 1/frac(k)))
        else: print('%.10f'%3)
    except EOFError:
        break