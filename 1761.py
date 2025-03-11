import math

while True:
    try:
        a, b, c = map(float, input().split(' '))
        print('%.2f' %(5 * (math.tan(a * 3.141592654 / 180) * b + c)))
    except EOFError:
        break