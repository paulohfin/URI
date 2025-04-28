def fat(a):
    if a < 2:
        return 1 
    else:
        return a * fat(a - 1)

while True:
    try:
        a, b = map(int, input().split(' '))
        print(fat(a) + fat(b))
    except EOFError:
        break