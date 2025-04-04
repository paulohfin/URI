def printa(n):
    if n < 10:
        print(n, end='')
    elif n == 10:
        print('A', end='')
    elif n == 11:
        print('B', end='')
    elif n == 12:
        print('C', end='')
    elif n == 13:
        print('D', end='')
    elif n == 14:
        print('E', end='')
    elif n == 15:
        print('F', end='')

def hexa(n):
    if n > 15:
        r = n% 16
        hexa(int(n/16))
        printa(r)
    else:
        printa(n)

while True:
    try:
        n = int(input())
        
        hexa(n)
        print()
    except EOFError:
        break 