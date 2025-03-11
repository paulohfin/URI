def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

while True:
    try:
        a, b = map(int, input().split(' '))
        
        div = mdc(a, b)
        diva = a / div 
        divb = b / div
        
        print(int(diva * 2 + divb * 2))
    except EOFError:
        break